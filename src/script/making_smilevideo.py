import cv2
import os
import sys
import shutil
import datetime
from time import sleep


def making_smilevideo(startframe,endframe):
    print("making_smilevideo_function")
    sleep(2)
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    output_dir_path = '../data/output_video/'
    if os.path.exists(output_dir_path) == False:
        os.mkdir(output_dir_path)

    dt_now = datetime.datetime.now()
    timestamp=dt_now.strftime('%Y%m%d%H%M%S')
    output_file = output_dir_path+'smile_video'+ timestamp +'.mp4'

    video = cv2.VideoWriter(output_file, fourcc, 30.0, (500, 500))
    for i in range(startframe,endframe):
        file_path = '../making_dataset/tempimg/faceimg'+str(i)+'.jpg'
        img = cv2.imread(file_path)
        img = cv2.resize(img, (500,500))
        video.write(img)
    print("video has made.")
    video.release()
