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
from get_userdata import get_users_data #userのcsvdataを数値として取得する
from making_plotdata import making_plot #グラフをplotする
from calc_difference import calc_dif
from get_rankingdata import get_rankingdata
from getindex import get_index
from userdatasave import user_data_save


if __name__ == '__main__':
    #wating画面の作成

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
        #モード0として管理
        mode =0
        csv_path,file_num = smile_capture(user_dir)#引数なしで実行する
        tempdir_cleaner()
        csv_file = csv_integrate(user_dir,csv_path,file_num,mode)
        print("csvfile:{}".format(csv_file))
        users_data_list=get_users_data(csv_file,mode)#userのcsvデータの塊を入手
        making_plot(users_data_list,user_dir)
        data_set_list = get_users_data("../data/output_csv/",1)#それぞれのデータセットのcsvの塊を入手
        difference = calc_dif(users_data_list,data_set_list)#2乗差を取得
        csv_list = glob.glob("../data/output_csv/*") #csvのリスト
        video_list= glob.glob("../data/output_video/*") #outputのvideoリスト
        csv_list.sort() #並び替え
        video_list.sort() #並び替え
        #print("csv:{}".format(csv_list)) #デバック
        #print("video:{}".format(video_list))#デバック
        #print("difference:{}".format(difference))#デバック
        #randomで5種類データを選ぶ必要あり => 値の差分
        index_list = get_index(difference) #listの中から選ぶための index_list作成
        choice_video_list = []
        for i in index_list:
            choice_video_list.append(video_list[i])
        print(choice_video_list)
        ranking = get_rankingdata(choice_video_list) #表示してランキングデータ取得
        print(ranking)
        user_data_save(user_dir,choice_video_list,ranking)
        print("finish")
        #userdirにランキングデータを保存する => 一番好みと答えた笑顔動画見せる
        #smileの画像をたくさん表示する => 動画生成の時に一番最後のimgpathの画像を保存する処理を書く
        #↑今日のやること！！！ +　動画のDL(芸能人人気ランキング的なものを40個DLする)
        #これは実験用
    else:
        #モード1として管理
        mode =1
        dir_path = str(sys.argv[1])
        files_list_path = dir_path+ "*.mp4"
        print(files_list_path)
        files_list = glob.glob(files_list_path)
        print(len(files_list))
        for file in files_list:
            csv_path,file_num = smile_capture_fromvideo(file)#dirpathを指定する
            if csv_path =="":
                pass
            else:
                tempdir_cleaner()
                csv_files = csv_integrate(user_dir,csv_path,file_num,mode)#csvのファイルがリターン
                print("csvfiles:{}".format(csv_files))
                data_set_list = get_users_data(csv_files,mode)#それぞれのデータセットのcsvの塊を入手
                making_plot(data_set_list,"")
        os.rmdir(user_dir)
        print("finish making dataset.")
            #これはデータセット作る時用
