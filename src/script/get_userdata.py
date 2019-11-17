#csvのデータ処理
import os
import sys
import shutil
import glob
import datetime
import csv
from time import sleep

def get_users_data(csv_dir,mode):
    dir_path = csv_dir
    csv_list =[]
    if mode ==0:
        csv_list.append(dir_path)

    elif mode ==1:
        csv_list_path = dir_path+ "*.csv"
        csv_list = glob.glob(csv_list_path)
    users_data_list =[]
    print("usersdata:{}".format(users_data_list))
    #print(csv_list)
    for csv_file in csv_list:
        with open(csv_file) as csv_f:
            reader = csv.reader(csv_f)
            l = [row for row in reader]
            users_data_list.append(l)

    #print(users_data_list[0][3][2])
    #print(users_data_list[0][0][0])
    #users_data_list[ユーザー指定][フレーム指定(0はヘッダー)][要素指定]
    #CSVごと,列ごとで取得　ex: users_data_list[0][0][0]ならば"face"を取得,users_data_list[0][0][1]ならば"confidence"を取得可能
    return users_data_list
    """
    csvから得られる要素
    0: face_id, 1:confidence, 2~4:左目の視線方向(x,y,z), 5~7:左目の視線方向(x,y,z),
    8~10: 視線方向の平均値, 11~65: 目の位置(２次元) (x),66~121: 目の位置(２次元) (y),
    122~177: 目の位置(3次元)(x), 178~233: 目の位置(3次元)(y), 234~289: 目の位置(3次元)(z),
    290~295: カメラ角度, 296~363: ２次元顔のパーツ位置(x),364~432: ２次元顔パーツ位置(y) Dlibと同じ
    (顔パーツ: 0~16 輪郭, 17~21　左眉, 22~26　右眉, 27~35 鼻, 36~41 左目, 42~47 右目, 48~67　口)
    433~499 :3次元m顔パーツ位置(x),500~567 :3次元m顔パーツ位置(y), 567~635 :3次元m顔パーツ位置(z),
    636~675 :顔の個人差や表情差を含んだ顔形状を表すモデルの値(スケール,回転,置き換え,軟質ポイント)
    676~692 :FAUの5スケール, 693~710: FAUの0,1判定
    (happinessのunitは1,6,10,12,14,20) => 676,680,683,684,685,688(強度),693,697,700,701,702,705(0,1判定)
    => 6と12で笑顔の判断ができそう
    => 636 に顔の補正スケールが入ってる => ずれの度合いが近いほどその人と顔が類似していることになる！ users_data[user][フレーム][636]　で入手

    参照(FAUの動きまとめ)
    https://imotions.com/blog/facial-action-coding-system/

    """


if __name__ == '__main__':
    dir_path = "../data/output_csv/"
    users_data_list = get_users_data(dir_path)
    print(users_data_list)
