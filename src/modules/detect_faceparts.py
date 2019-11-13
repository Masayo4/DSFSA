import cv2
import dlib
import sys
import os
import datetime
import glob
import random
import shutil

'''
68点モデルの場合
顔のパーツの番号(検出している人):
基本左側から番号
0~16:輪郭(0が左端で時計回り), 17~21:左眉毛, 22~26:右眉毛, 27~30:鼻筋, 31~35:鼻,(鼻の頭は30)
36~41:左目(36が左端で時計回り),42~47:右目(42が左端で時計回り)
48~59:口外側(48が左端で時計回り), 60~67:口内側(60が左端で時計回り)
'''


def faceparts_detector(dir):
    #print("dir:{}".format(dir))
    img_list_path = dir+ "*.jpg"
    img_list = glob.glob(img_list_path)
    print(img_list)
    #globで.jpgのファイルを全て取ってくる
    if len(img_list) == 0:
        print("No_img_file.")
        quit()

    #img_list = glob.glob("imgdata/face_img/*.jpg") 直書きするとこんな感じ
    detector = dlib.get_frontal_face_detector()
    predictor_file_path = "models/shape_predictor_68_face_landmarks.dat"
    predictor = dlib.shape_predictor(predictor_file_path)
    #モデルのセッティング

    each_point_arr = []
    index = 1 #画像が複数あった場合の処理用

    for img in img_list:
        frame = cv2.imread(img)
        dt_now = datetime.datetime.now()
        timestamp=dt_now.strftime('%Y%m%d%H%M%S')
        dets = detector(frame[:,:,::-1])

        if dir == "imgdata/user_face/":
            filename ="imgdata/face_img/face_" + timestamp+"_"+str(index)+".jpg"
            cv2.imwrite(filename, frame) #データとしてface_imgに移動しておく
            #dets = detector(frame[:,:,::-1])
            if len(dets) >0:
                parts = predictor(frame,dets[0]).parts()
                each_point_arr.append(parts)
                output = frame *0.5
                before_part = 0
                l = 0 #line_draw のlでindex管理
                cbi = random.randint(0,255) #color_blue_index
                cgi = random.randint(0,255) #color_blue_index
                cri = random.randint(0,255) #color_blue_index
                for i in parts:
                    cv2.circle(output,(i.x,i.y),3,(cbi,cgi, cri),-1)
                    if l == 0 or l ==17 or l ==27 or l ==31 or l ==36 or l ==42 or l ==48 or l ==60:
                        pass
                    else:
                        cv2.line(output,(before_part.x,before_part.y),(i.x,i.y),(cbi,cgi, cri),1)
                    before_part = i
                    l = l +1
                cv2.circle(output,(parts[30].x,parts[30].y),3,(0,255,0),-1) #鼻頭の色を塗る
                #cv2.line(output,(parts[0].x,parts[0].y),(parts[1].x,parts[1].y),(255,0, 0),1) ライン描画？
                #cv2.imshow("output",output)
                output_img_filename ="imgdata/output_img/face_" + timestamp+"_"+str(index)+"_output.jpg"
                #print(output_img_filename)
                cv2.imwrite(output_img_filename, output)
                print("done")
                index = index +1 #複数あった場合はここでindexを振る

            for p in glob.glob('imgdata/user_face/*.jpg', recursive=True):
                if os.path.isfile(p):
                    os.remove(p)#user_face_img　を消去する
                    print("user_face_img cleaned")
        else:
            filename = glob.glob('imgdata/face_img/*.jpg', recursive=True)


            if len(dets) >0:
                parts = predictor(frame,dets[0]).parts()
                each_point_arr.append(parts)
        #cv2.imshow("output",frame) デバック用

    cv2.destroyAllWindows()

    return each_point_arr,filename
    #それぞれ検出した顔の特徴点の座標データをlistで返す

if __name__ == '__main__':
    #img_list = glob.glob("imgdata/face_img/*.jpg")
    dir_path = "imgdata/user_face/"
    arr= faceparts_detector(dir_path)
    #取ってきた位置情報はarr[番目][顔のindex]で呼び出し可能(片方ずつの場合は,後ろに .x や .y　をつける)
