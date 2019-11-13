import cv2
import dlib
import sys
import os
import datetime
import math

from detect_faceparts import faceparts_detector
#他のスクリプトから関数呼び出し
'''
顔のパーツの位置を計算する
鼻頭を中心にそこからどれぐらいの距離に対象とする部分が存在するのかを計算する関数
(距離は2点間距離の計算式で出しに行く)
'''
def facebalance_calculator(userface,dbfaces):
    user_facedata_list = userface
    user_facebalance_list = []

    for user_face_data in user_facedata_list:
        center = user_face_data[30] #鼻頭の位置
        user_facebalance_data = []
        for i in range(len(user_face_data)):
            dist = math.sqrt((user_face_data[i].x-center.x)**2 + (user_face_data[i].y-center.y)**2) #三平方での直線距離を出しに行く
            #print ("距離:{}".format(dist))
            user_facebalance_list.append(dist)
    #ユーザーの顔用
    #print("userface:{},cal{}".format(user_facedata_list,user_facebalance_list)) デバッグ用
    db_users_facedata_list = dbfaces
    db_users_facebalance_list = []
    n = 1
    for db_user_face_data in db_users_facedata_list:

        center = db_user_face_data[30] #鼻頭の位置
        db_user_facebalance_data = []
        for i in range(len(db_user_face_data)):
            dist = math.sqrt((db_user_face_data[i].x-center.x)**2 + (db_user_face_data[i].y-center.y)**2) #三平方での直線距離を出しに行く
            #print ("距離:{}".format(dist))
            db_user_facebalance_data.append(dist)

        db_users_facebalance_list.append(db_user_facebalance_data)
        n = n +1
    #print("dbuserface:{},dbcal{}".format(db_users_facedata_list,db_users_facebalance_list))


    #print("user_facebalance_data:{}".format(users_facebalance_list)) #デバック用
    #スコア算出
    cal_result_arr = [] #それぞれの結果をいれておく配列
    base_score = user_facebalance_list #一番最初の時に使う
    #print("basescore:{}".format(base_score))
    for score in db_users_facebalance_list:
        cal_result = 0 #描く画像2マイに対するループ
        cal_arr = [] #平均値で得点のときに使う配列
        #print("cal_result1:{}".format(cal_result))

        for i in range(len(base_score)):
            if i == 30:
                pass #両方とも値が0なので計算できない
            else:
                #print("score[i]:{}とbase[i]{}".format(score[i],base_score[i]))
                cal_temp = 1 - abs(score[i]-base_score[i])/base_score[i]
                #print("cal_temp:{}".format(cal_temp))
                #ずれのパーセンテージを出す
                #print("caltemp:{}".format(cal_temp))
                cal_arr.append(cal_temp) #平均を出すための配列作成

        for average in cal_arr:
            #print("ave:{}".format(average))
            cal_result = cal_result+average #合計値の算出
        cal_result = (cal_result/67)*100 #67要素数で割る(30は省いているので)
        #print(cal_result) デバッグ用
        cal_result_arr.append(cal_result) #結果保存関数へのappend
    print("類似度は{}".format(cal_result_arr))
    #print(len(cal_result_arr))

    return cal_result_arr


if __name__ == '__main__':
    dir_path = "imgdata/face_img/"
    arr= faceparts_detector(dir_path)

    facebalance_calculator(arr)
