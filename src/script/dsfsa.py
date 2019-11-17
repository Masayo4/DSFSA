import cv2
import os
import sys
import shutil
import datetime
from time import sleep
from triming_smile import smile_capture
from dirmanager import sys_init,tempdir_cleaner #manager.py よりdirの整理系
from making_smilevideo import making_smilevideo #making_smilevideoよりvideoの作成
from openface_manager import csvmanager,csv_integrate,openface_run #openface関係



if __name__ == '__main__':
    get_img_path = "../making_dataset/tempimg/"
    #dataset用のpath
    dt_now = datetime.datetime.now()
    
    timestamp=dt_now.strftime('%Y%m%d%H%M%S')
    user_dir = "../data/plot/"+timestamp
    os.mkdir(user_dir)
    #ユーザーごとにデータを整理するためのdirを作成する


    sys_init()
    if len(sys.argv) == 1:
        csv_path,file_num = smile_capture("")
    else:
        csv_path,file_num = smile_capture(sys.argv[1])
    tempdir_cleaner()
    csv_integrate(csv_path,file_num)
    #このあと表示部分の作成をする
