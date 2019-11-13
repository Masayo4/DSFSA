import cv2
import dlib
import sys
import os

from show_start_phase import waiting_next
from take_picture import take_user_picture
from detect_face import face_detector
from detect_faceparts import faceparts_detector
from facebalance_cal import facebalance_calculator
from choice_img import choice_img,making_showimg

if __name__ == '__main__':
    #phase_index = 0
    user_id = 1 #ここは動的に変化させる
    user_face_parts = [] #ユーザーの特徴点いれる
    database_faces_parts = [] #データベースにある顔の特徴量
    waiting_next() #最初の画面
    user_face_img_path = take_user_picture("imgdata/taking_pic/",user_id) #user_faceに保存する
    save_dir_name = face_detector(user_face_img_path)  #user_faceからとってくる
    #print("特徴点座標:{}".format(faceparts_detector(save_dir_name)))
    database_faces_parts, img_name_list = faceparts_detector("imgdata/face_img/") #dbからのデータとおよび,imgfileのpathlist
    user_face_parts, user_img_name = faceparts_detector(save_dir_name) #ユーザーのデータおよびimgfileのpath
    #print("dbの顔データ特徴点:{}".format(database_faces_parts))
    #print("img_list:{},userimg:{}".format(database_faces_parts, img_name_list))
    score_arr = facebalance_calculator(user_face_parts,database_faces_parts)
    #print("score_arr:{}".format(score_arr)) #顔の類似度(今は鼻からのパーツの位置)
    #print(img_name_list)
    choice_score = choice_img(img_name_list)
