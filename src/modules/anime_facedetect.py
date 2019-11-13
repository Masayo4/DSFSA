#https://github.com/nagadomi/lbpcascade_animeface 参考
'''
画像の中から顔を検出してそのキャラクターの顔を保存するプログラムの作成
'''
import cv2
import sys
import datetime
import os

def anime_facedetector(input_img):
    img_file = input_img #画像を第２引数で呼び出す
    cascade_file = "../../data/dataset/lbpcascade_animeface.xml"
    file_exist = os.path.exists(cascade_file)
    print("cascade_exist:{}".format(file_exist))

    cascade = cv2.CascadeClassifier(cascade_file) #カスケードファイルの読み込み
    img = cv2.imread(img_file,cv2.IMREAD_COLOR) #画像をopencvで読み込む
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray) #ヒストグラム平坦化(ボヤけているものをはっきりさせる,コントラストがはっきりする)

    dt_now = datetime.datetime.now()
    timestamp=dt_now.strftime('%Y%m%d%H%M%S')
    savedir_path = "../img/output/"+timestamp
    img_num = 0
    #dirの作成

    faces = cascade.detectMultiScale(gray,scaleFactor =1.1, minNeighbors =5, minSize=(24,24))
    #検出するオブジェクトの調整
    for rect in faces:
        cv2.rectangle(img,(rect[1],rect[0]),(rect[1] + rect[3],rect[0] + rect[2]),(255,0,0),2) #四角で囲む
        saveimg_path= savedir_path + str(img_num) + "_img_output.png"
        cv2.imwrite(saveimg_path,img[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]])
        img_num = img_num +1

    cv2.imshow("Result",img)
    cv2.waitKey(0)

    if len(sys.argv) !=2:
        sys.stderr.write("usage: python anime_facedetect.py img_path")
        sys.exit(-1)

if __name__ == '__main__':
    anime_facedetector(sys.argv[1])
