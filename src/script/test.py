import os
import sys
import datetime
import glob



dir_path = "../data/output_csv/"

files_list_path = dir_path+ "*.csv"
files_list = glob.glob(files_list_path)
print(files_list)


import math

difference = [0.22893946485260774, 0.08033175510204053, 0.03855379000141717, 0.0,0.423]

add_indexlist = list(enumerate(difference))
get_index_list = sorted(enumerate(difference), key=lambda x: x[1])

print(get_index_list[0][0]) #自分の表示
print(get_index_list[-1][0]) #一番遠い人
print(get_index_list[1][0]) #一番近い人
median_upper = math.ceil(len(get_index_list)/2)
medien_lower = math.floor(len(get_index_list)/2)
print("index:{}:{}".format(median_upper,medien_lower))
print(get_index_list[median_upper][0]) #中央上
print(get_index_list[medien_lower][0]) #中央下



#print("maxindex:{},minindex:{},randindex:{}".format(max_index,min_index,rand_index))
