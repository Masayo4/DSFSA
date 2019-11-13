import cv2
import sys
import os
import datetime
import glob
import random
import numpy as np
from PIL import Image


def choice_img(img_array):
    ranking_list = []
    #いい感じにばらけさせて表示する方法を考える　
    dt_now = datetime.datetime.now()
    timestamp=dt_now.strftime('%Y%m%d')
    save_path = 'imgdata/show_img/' + timestamp +"_show.jpg"
    making_showimg(img_array,save_path)

    img = cv2.imread(save_path)
    cv2.namedWindow('show_img',cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("show_img",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    while True:
        cv2.imshow('show_img',img)
        cv2.moveWindow('show_img', 0, 0)
        k = cv2.waitKey(0)

        if k == "27" or k == ord("q"):
            cv2.destroyAllWindows()
            break
        elif k == ord("1"):
            if ranking_list.count(1) == 0:
                ranking_list.append(1)
        elif k == ord("2"):
            if ranking_list.count(2) == 0:
                ranking_list.append(2)
        elif k == ord("3"):
            if ranking_list.count(3) == 0:
                ranking_list.append(3)
        elif k == ord("4"):
            if ranking_list.count(4) == 0:
                ranking_list.append(4)
        elif k == ord("5"):
            if ranking_list.count(5) == 0:
                ranking_list.append(5)
        elif k == ord("c"):
            ranking_list = []
        else:
            pass

        if len(ranking_list) == 5:
            break
    print("user_favorite:{}".format(ranking_list))
    return ranking_list



def making_showimg(img_array,path):
    read_img_list = []
    img_num = 1
    for img in img_array:
        im = cv2.imread(img)
        cv2.putText(im, str(img_num), (25, 50), cv2.FONT_HERSHEY_PLAIN, 4, (0, 255, 0), 5, cv2.LINE_AA)
        read_img_list.append(im)
        img_num = img_num +1
    show_img = cv2.hconcat(read_img_list)
    cv2.imwrite(path,show_img)

if __name__ == '__main__':
    score_arr = [76.43736259648199, 87.42675761873953, 86.6797796979763, 72.37043764464823, 77.78615489691661]
    img_arr = ['imgdata/face_img/face_20191103130105_1.jpg', 'imgdata/face_img/face_20191103130118_1.jpg', 'imgdata/face_img/face_20191103130114_1.jpg', 'imgdata/face_img/face_20191103130809_1.jpg', 'imgdata/face_img/face_20191103130109_1.jpg']
    choice_img(img_arr)
