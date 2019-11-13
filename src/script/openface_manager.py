import cv2
import os
import sys
import shutil
import datetime
from time import sleep
import glob
import pandas as pd
from dirmanager import processed_cleaner

#os.system("build/bin/FaceLandmarkVid -f videopath")　#C++の動画用コンパイルファイルを呼び出すことができる
#os.system("build/bin/FaceLandmarkImg -f imgpath") #C++の画像用コンパイルファイルを呼び出すことができる(画像1枚用)
#os.system("build/bin/FaceLandmarkImg -fdir dirpath/") #C++の画像用コンパイルファイルを呼び出すことができる(dir用)


def openface_run(): #openfaceコンパイルファイルを走らせる
    print("openface run")
    os.system("../OpenFace/build/bin/FaceLandmarkImg -fdir ../making_dataset/tempimg") #openfeceのコンパイルファイルを動かす
    print("openfece process finish")
    csv_output_path = "processed/"
    return csv_output_path

def csvmanager(): #csvを移動させる
    print("csvmanager")
    if os.path.exists("processed/") == True:
        processed_cleaner()

    now_dir = openface_run()
    csv_list_path = now_dir+ "*.csv"
    csv_list = glob.glob(csv_list_path)
    #print(csv_list)
    file_num = len(csv_list)

    if len(csv_list) ==0:
        print("csvfile dosen't exist")

    for csv_file in csv_list:
        pwd_path = csv_file
        move_path = "../data/csv/"
        print("pwd:{},move:{}".format(pwd_path,move_path))
        new_path = shutil.move(pwd_path,move_path)

    shutil.rmtree(now_dir)
    return move_path,file_num

def csv_integrate(dir_path,num):
    csv_dir = dir_path
    file_num = num
    files = sorted(glob.glob('../data/csv/*.csv'))

    csv_list = []
    for file in files:
        csv_list.append(pd.read_csv(file))

    merge_csv = pd.concat(csv_list)
    dt_now = datetime.datetime.now()
    timestamp=dt_now.strftime('%Y%m%d%H%M%S')
    file_name = "../data/output_csv/"+timestamp +".csv"
    merge_csv.to_csv(file_name,encoding='utf_8',index=False)
    shutil.rmtree(csv_dir)
    os.mkdir(csv_dir)
    print("finish.")




if __name__ == '__main__':
    csv_path,file_num = csvmanager()
    csv_integrate(csv_path,file_num)
    #csv_integrate("../data/csv/",21)
