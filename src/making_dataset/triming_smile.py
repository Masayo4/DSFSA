"""
youtube等の動画から笑顔のタイミングを取得する
笑顔のタイミング1.5秒前からの動画をトリミングしていくスクリプトを書く
smileかどうかは何で判断しようか...? => opencvのsmileカスケードでいいかな？
"""

import cv2
import os
import sys
import shutil
import datetime
from time import sleep

def sys_init():
    print("sysinit_function")
    dirpath = "tempimg/"
    if os.path.exists(dirpath) == True:
        shutil.rmtree(dirpath)
    os.mkdir(dirpath)



def smile_capture(video_path):
    print("smilecapture_function")
    file = video_path
    show_window_name = 'now_frame'
    #表示するwindow nameを統一するための変数
    face_detect_cascade_path = "../modules/haarcascades/haarcascade_frontalface_default.xml"
    face_detect_cascade = cv2.CascadeClassifier(face_detect_cascade_path)
    #顔の検出のためのカスケード

    smile_cascade_path = "../modules/haarcascades/haarcascade_smile.xml"
    smile_cascade = cv2.CascadeClassifier(smile_cascade_path)
    #笑顔検出のためのカスケード
    print("finish_loading_cascade")
    frame_counter = len(os.listdir("tempimg/")) #フレームを最初から保存する
    smile_frame = 0 #smileのフレーム数のカウント
    delete_file_counter = 0 #60フレームで動画を作るのでフォルダの中は常に60枚の画像にしておく
    window_manager = 0 #windowの切り替え

    if file == "":
        cap = cv2.VideoCapture(0) #webカメラなどデバイスから動画を検出する場合は引数に数値にしていする
        print("start_from_webcam")
    else:
        cap = cv2.VideoCapture(file) #Videoからのキャプチャーをするときはこの引数に指定する
        print("use_video_file")

    while cap.isOpened():
        ret, frame = cap.read()
        #カメラ画像の取得開始
        if not ret:
            print("no_frame")
            break #frame数がなくなったら終了する

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #grayスケールに変換してから判別を行う
        face_list =face_detect_cascade.detectMultiScale(gray,scaleFactor = 1.21,minNeighbors = 15, minSize=(50,50))
        #顔の判定

        #トリミングするための処理

        if len(face_list) > 0: #顔を検出したら
            for x,y,w,h in face_list:
                face = frame[y:int((y+h)), x:int((x+w))] #顔の位置座標を取りに行く
                scale = 480 / h #大きさの調整
                face = cv2.resize(face, dsize=None, fx=scale, fy=scale) #比率をそのままに大きさを表示する
                file_name = "tempimg/faceimg"+str(frame_counter)+".jpg"
                frame_counter = frame_counter +1
                cv2.imwrite(file_name,face) #保存するためのもの

                face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                smile_detector =smile_cascade.detectMultiScale(face_gray,scaleFactor= 1.7, minNeighbors=20, minSize=(200, 100))
                #調整済みのパラメータ minsizeを工夫すると領域の中で小さい誤検出がなくなった
                #smileの判定
                if len(smile_detector) >0:
                    for x,y,w,h in smile_detector:
                        cv2.rectangle(face,(x,y),(x+w,y+h),(0,255,0),2)

                    #print("smile_detector_contents:{}".format(smile_detector))
                    #笑顔検出したときだけ切り抜くってやりたい  => うまく検出できたので, 一定フレーム数が溜まったら切り抜く形にする
                    cv2.imshow("face",face) #顔だけ切り抜いて表示する
                    cv2.moveWindow("face", 700, 0)

                    smile_frame = smile_frame +1

                    #print("smile_counter:{}".format(smile_frame))
                    #print("delete_file_counter:{}".format(delete_file_counter))
                    #print("frame_counter:{}".format(frame_counter))

                    if frame_counter >30:
                        if smile_frame >5: #このフレーム数を調整
                            making_smilevideo(delete_file_counter,frame_counter)
                            dir_cleaner()
                            frame_counter =0
                            smile_frame = 0
                            delete_file_counter = 0
                        else:
                            cv2.destroyWindow("face")
                            frame_counter = 0
                            smile_frame =0


        cv2.imshow(show_window_name,frame) #webカメラからの画像を取得し続ける
        cv2.moveWindow(show_window_name, 0, 0)


        if frame_counter > 60:
            delete_file_path = "tempimg/faceimg"+str(delete_file_counter)+".jpg"
            os.remove(delete_file_path)
            delete_file_counter = delete_file_counter +1

        key = cv2.waitKey(1)
        if key == 27 or key == ord("q"):
            dir_cleaner()
            break
    cap.release()
    cv2.destroyAllWindows()


def making_smilevideo(startframe,endframe):
    print("making_smilevideo_function")
    sleep(2)
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    output_dir_path = 'output_video/'
    if os.path.exists(output_dir_path) == False:
        os.mkdir(output_dir_path)

    dt_now = datetime.datetime.now()
    timestamp=dt_now.strftime('%Y%m%d%H%M%S')
    output_file = output_dir_path+'smile_video'+ timestamp +'.mp4'

    video = cv2.VideoWriter(output_file, fourcc, 30.0, (500, 500))
    for i in range(startframe,endframe):
        file_path = 'tempimg/faceimg'+str(i)+'.jpg'
        img = cv2.imread(file_path)
        img = cv2.resize(img, (500,500))
        video.write(img)
    print("video has made.")
    video.release()

def dir_cleaner():
    print("dir_cleaning")
    dirpath = "tempimg/"
    shutil.rmtree(dirpath)
    os.mkdir(dirpath)


if __name__ == '__main__':
    sys_init()
    if len(sys.argv) == 1:
        smile_capture("")
    else:
        smile_capture(sys.argv[1])
    dir_cleaner()

"""
参考URL:
https://note.nkmk.me/python-opencv-video-to-still-image/ フレームの切り出し
"""
