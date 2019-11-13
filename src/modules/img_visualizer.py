import cv2
import dlib
import sys
import os
import datetime
import glob
import re

def img_visualizer(dir):
    img_list_path = dir+ "*.jpg"
    img_list = glob.glob(img_list_path)
    #print(img_list)
    output_img_list = []
    for img_path in img_list:
        #print(re.search('output',img_path))
        if (re.search('output',img_path)) != None:
            output_img_list.append(img_path)
            #正規表現でoutputの画像を拾う
        else:
            pass
    #globで.jpgのファイルを全て取ってくる
    if len(img_list) == 0:
        print("No_img_file.")
        quit()

    i = 0 #複数枚あった場合の重ね順
    j = 1 #1枚ずつ重ねる
    for img in output_img_list:
        img1 = cv2.imread(output_img_list[i]) #ベースimg
        img2 = cv2.imread(output_img_list[j]) #重ねるimg
        blended = cv2.addWeighted(src1=img1,alpha=0.7,src2=img2,beta=0.5,gamma=0) #ここで透明度等調整
        cv2.imshow("blend_img",blended) #表示
        cv2.waitKey(0) #表示を終了させるための処理
        if j<len(output_img_list)-1:
            i = i+1
            j = j+1
        #可視化処理



if __name__ == '__main__':
    #img_list = glob.glob("imgdata/face_img/*.jpg")
    dir_path = "imgdata/face_img/"
    arr= img_visualizer(dir_path)
