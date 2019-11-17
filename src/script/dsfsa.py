import cv2
import os
import sys
import shutil
import datetime
import glob
from time import sleep
from triming_smile import smile_capture
from triming_smile_fromvideo import smile_capture_fromvideo
from dirmanager import sys_init,tempdir_cleaner #manager.py よりdirの整理系
from making_smilevideo import making_smilevideo #making_smilevideoよりvideoの作成
from openface_manager import csvmanager,csv_integrate,openface_run #openface関係
from get_userdata import get_users_data
from making_plotdata import making_plot



if __name__ == '__main__':
    get_img_path = "../making_dataset/tempimg/"
    #dataset用のpath
    dt_now = datetime.datetime.now()

    timestamp=dt_now.strftime('%Y%m%d%H%M%S')
    user_dir = "../data/users/"+timestamp+"/"
    os.mkdir(user_dir)
    #ユーザーごとにデータを整理するためのdirを作成する
    #dirごとにデータを呼び出す必要ありなので少し変更

    sys_init()
    if len(sys.argv) == 1:
        csv_path,file_num = smile_capture(user_dir)
        tempdir_cleaner()
        csv_file = csv_integrate(user_dir,csv_path,file_num,0)
        print("csvfile:{}".format(csv_file))
        users_data_list=get_users_data(csv_file,0)
        making_plot(users_data_list,user_dir)
        #これは実験用
    else:
        csv_path,file_num = smile_capture_fromvideo(sys.argv[1])
        tempdir_cleaner()
        csv_files = csv_integrate(user_dir,csv_path,file_num,1)#csvのファイルがリターン
        print("csvfiles:{}".format(csv_files))
        data_set_list = get_users_data(csv_files,1)
        making_plot(data_set_list,"")
        os.rmdir(user_dir)
        print("finish making dataset.")
        #これはデータセット作る時用
