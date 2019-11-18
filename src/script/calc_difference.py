from get_userdata import get_users_data
import os
import sys
import shutil
import datetime
import glob
import csv

def calc_dif(user,database):
    #minuend(惹かれる数)-subtrahend(引く数)=difference(計算結果)
    get_scale_index = 636
    minuend = user
    subtrahends = database
    subtrahends_list = []
    difference_square_list = []
    #print(len(minuend[0]))
    pmd_scale = 0
    for i in range(len(minuend[0])):
        if i ==0:
            pass
        else:
            pmd_scale = pmd_scale + float(minuend[0][i][get_scale_index])
    pmd_scale_average = pmd_scale/(len(minuend[0])-1)

    pmd_scales = 0
    for i in range(len(database)):
        for j in range(len(subtrahends[i])):
            if j ==0:
                pass
            else:
                pmd_scales = pmd_scales + float(subtrahends[i][j][get_scale_index])
        pmd_scales = pmd_scales/(len(subtrahends[i])-1)
        subtrahends_list.append(pmd_scales)
        pmd_scales =0

    #print("user_pmd:{}".format(pmd_scale_average))
    #print("database_pmd:{}".format(subtrahends_list))
    for subtrahend in subtrahends_list:
        difference_square = (subtrahend-pmd_scale_average)**2
        difference_square_list.append(difference_square)
    #print("二乗差:{}".format(difference_square_list))


    return difference_square_list
    #return pmd_scale,fau_6,fau_12


if __name__ == '__main__':
    user_data_dir = "../data/users/20191117163851/20191117163915.csv"
    database_data_dir = "../data/output_csv/"
    userdata = get_users_data(user_data_dir,0)
    databasedata = get_users_data(database_data_dir,1)
    #print("userdata:{}".format(len(userdata)))

    #pmd,fau_6,fau_12 = calc_dif(userdata,databasedata)
    calc_dif(userdata,databasedata)
