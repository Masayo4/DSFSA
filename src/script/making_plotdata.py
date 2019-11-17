import matplotlib.pyplot as plt
import math
import numpy as np

from get_userdata import get_users_data

def making_plot(data):#データを確認する用
    users_data = data
    fau_name =[6,12]
    get_faur_index = [680,684]#強度
    get_fauc_index = [697,701]#0,1判定

    #print("test:{}".format(len(users_data)))

    for user in range(len(users_data)):
        row_count = 1
        column_count = 3
        graphs_count = row_count*column_count
        #グラフの個数の指定
        axes = []#保存用
        fig = plt.figure(figsize=(9,6))
        single_plot = 1#PMDの値は1種類だけのグラフとする
        for i in range(1,graphs_count+1):
            plot_y_1 = []
            plot_y_2 = []
            plot_x = []
            axes.append(fig.add_subplot(row_count, column_count, i))#複数個グラフを表示するためのフォーマット作成
            for x in range(len(users_data[user])):
                if x == 0:#0番目にはラベルが入っているので無視
                    pass
                else:
                    if single_plot ==1:
                        y1 = float(users_data[user][x][636]) #顔の類似度のプロット
                        plot_y_1.append(y1)
                        plot_x.append(x)
                        axes[i-1].plot(plot_x,plot_y_1, color ="green", linewidth= 2) #類似
                        plot_memo = "PMD_scale"#平均顔への修正
                        plt.title(plot_memo)
                        #print("x:{},scale:{}".format(plot_x,plot_y_1))
                        #print("flag:{}".format(single_plot)) デバッグ用
                    else:
                        #print("flag:{}".format(single_plot))
                        #print("xlen:{},y1len:{},y2len{}".format(len(plot_x),len(plot_y_1),len(plot_y_2)))
                        #print("index:{}".format(i-2)) デバッグ用
                        y1 = float(users_data[user][x][get_faur_index[i-2]]) #強度用
                        y2 = float(users_data[user][x][get_fauc_index[i-2]]) #0,1用
                        plot_y_1.append(y1)
                        plot_y_2.append(y2)
                        plot_x.append(x)
                        #print("x:{},y1:{},y2{}".format(plot_x,plot_y_1,plot_y_2))
                        axes[i-1].plot(plot_x,plot_y_1, color ="blue", linewidth= 2) #強度
                        axes[i-1].plot(plot_x,plot_y_2, color ="red", linewidth= 1) #判定
                        plot_memo = "FAU" + str(fau_name[i-2])#FAUの値を指定
                        plt.title(plot_memo)
                        #print("xlen:{},y1len:{},y2len{}".format(len(plot_x),len(plot_y_1),len(plot_y_2)))
            single_plot = single_plot-1

        fig.subplots_adjust(wspace=0.3, hspace=0.3) #隙間の調整
        #plt.show()#表示する
        dt_now = datetime.datetime.now()
        timestamp=dt_now.strftime('%Y%m%d%H%M%S')
        file_name = "../data/plot/"+timestamp +".png"
        plt.savefig(file_name) #画像としてファイルの保存をする
        #plt.close()



if __name__ == '__main__':
    dir_path = "../data/output_csv/"
    users_data_list = get_users_data(dir_path)
    making_plot(users_data_list)
