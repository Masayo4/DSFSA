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
import glob
from time import sleep
from dirmanager import sys_init,tempdir_cleaner #manager.py よりdirの整理系
from making_smilevideo import making_smilevideo #making_smilevideoよりvideoの作成
from openface_manager import csvmanager #openface関係

def smile_capture_fromvideo(file):
    print("smilecapture_function")
    #file = dir_path 元
    file = file
    print(file)

    show_window_name = 'now_frame'
    #表示するwindow nameを統一するための変数
    face_detect_cascade_path = "../dataset/haarcascades/haarcascade_frontalface_default.xml"
    face_detect_cascade = cv2.CascadeClassifier(face_detect_cascade_path)
    #顔の検出のためのカスケード

    smile_cascade_path = "../dataset/haarcascades/haarcascade_smile.xml"
    smile_cascade = cv2.CascadeClassifier(smile_cascade_path)
    #笑顔検出のためのカスケード
    print("finish_loading_cascade")
    frame_counter = len(os.listdir("../making_dataset/tempimg/")) #フレームを最初から保存する
    smile_frame = 0 #smileのフレーム数のカウント
    delete_file_counter = 0 #60フレームで動画を作るのでフォルダの中は常に60枚の画像にしておく
    window_manager = 0 #windowの切り替え
    cap_smile = 0
    file_num = 0

    tempdir_cleaner()
    cap = cv2.VideoCapture(file) #Videoからのキャプチャーをするときはこの引数に指定する
    print("use_video_file")
    cap_smile = 5 #動画ファイルだったら5フレーム継続

    while cap.isOpened():
        ret, frame = cap.read()
        #カメラ画像の取得開始
        if not ret:
            print("no_frame")
            return "", 0

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
                file_name = "../making_dataset/tempimg/faceimg"+str(frame_counter)+".jpg"
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

                    if frame_counter >15:
                        if smile_frame >cap_smile: #このフレーム数を調整
                            output_file = making_smilevideo(delete_file_counter,frame_counter) #making_smilevideo.py を呼び出す
                            csv_path,file_num = csvmanager()
                            if cap_smile == 5:
                                tempdir_cleaner()
                                cap.release()
                                cv2.destroyAllWindows()
                                smile_frame =0
                                return csv_path,file_num
                        else:
                            cv2.destroyWindow("face")
                            frame_counter = 0
                            smile_frame =0


        cv2.imshow(show_window_name,frame) #webカメラからの画像を取得し続ける
        cv2.moveWindow(show_window_name, 0, 0)

        file_counter = glob.glob("../making_dataset/tempimg/")
        if frame_counter > 20 and len(file_counter)>20:
            delete_file_path = "../making_dataset/tempimg/faceimg"+str(delete_file_counter)+".jpg"
            os.remove(delete_file_path)
            delete_file_counter = delete_file_counter +1

        key = cv2.waitKey(1)
        if key == 27 or key == ord("q"):
            tempdir_cleaner()
            break
    cap.release()
    cv2.destroyAllWindows()



"""
参考URL:
https://note.nkmk.me/python-opencv-video-to-still-image/ フレームの切り出し
"""
