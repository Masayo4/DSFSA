#68点モデルの使用
import cv2
import sys
import os
import datetime
from PIL import Image

'''
facedetectして顔画像を切り出すモジュール
画像は500*500 px に大きさを調整する
'''

def face_detector(img):
    #dirの構造がない時は自動でdirの作成を行う
    if os.path.exists("./imgdata") ==False:
        os.mkdir("./imgdata/face_img")

    origin_img = cv2.imread(img)
    img = origin_img.copy()
    #imgの読み込みを行う

    cascade_path = "haarcascades/haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(cascade_path)
    #顔判定を行うカスケードの設定(openCVについているデフォルトのものを使用)
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #facedetectをするときはgrayスケールで読み込みを行う
    faces_list = cascade.detectMultiScale(gray_img,scaleFactor =1.1, minNeighbors =3,minSize=(100,100))

    #print(faces_list)#検出した顔の個数をカウントするためのリスト
    if len(faces_list) == 0:
        print("Falled or Noface")
        quit()

    index = 1 #顔が複数あった場合の処理用

    #検出した顔それぞれを保存する
    for (x,y,w,h) in faces_list:
        face_img = origin_img[y:int((y+h)), x:int((x+w))]
        scale = 480 / h
        face_img = cv2.resize(face_img, dsize=None, fx=scale, fy=scale)
        dt_now = datetime.datetime.now()
        timestamp=dt_now.strftime('%Y%m%d%H%M%S')
        save_dir_name = "imgdata/user_face/"
        filename =save_dir_name+ "face_" + timestamp+"_"+str(index)+".jpg"
        cv2.imwrite(filename, face_img)
        #ここで一回画像として書き出しを行う
        output = Image.open(filename)
        img_resize = output.resize((500, 500))
        img_resize.save(filename)
        #ここで画像のサイズ調整を行う

        index = index +1 #複数あった場合はここでindexを振る

        return save_dir_name




if __name__ == '__main__':
    img_path = sys.argv[1] #第一引数に検出した画像のpathを指定する
    face_img = face_detector(img_path)
    '''
    メモ:
    一枚ずつの指定がこの関数では可能. 最終的には大量の処理を行いたいので, dirから画像pathをlist化して
    for文で処理し続けさせる関数 or スクリプト複数行を書く 20191009
    '''
