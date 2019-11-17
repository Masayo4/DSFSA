#動画の分割を行う
import cv2
import os
import sys
import shutil
import glob
import datetime

def video_split(dir_path):
    movie_dir = dir_path + "*"
    movie_list = glob.glob(movie_dir)
    print("movie_list:{}".format(movie_list))
    for movie in movie_list:
        cap = cv2.VideoCapture(movie)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        if cap.isOpened():
            length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            #print(length) 総フレーム数
            for i in range(length):
                ret, frame = cap.read()
                filename = "dataset_movie/temp_img/img_"+str(i)+".jpg"
                cv2.imwrite(filename,frame)

                if i%300 == 0 and i != 0:
                    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
                    base_movie_dir = "dataset_movie/temp_img/*.jpg"
                    base_movie_list = glob.glob(base_movie_dir)
                    base_movie_list = sorted(base_movie_list)
                    dt_now = datetime.datetime.now()
                    timestamp=dt_now.strftime('%Y%m%d%H%M%S')

                    output_file = 'dataset_movie/'+timestamp+ str(i)+'.mp4'
                    #print("width:{},height:{}".format(width,height))
                    video = cv2.VideoWriter(output_file, fourcc, 30.0, (width, height))
                    #print(base_movie_list)
                    for img in base_movie_list:
                        write_img = cv2.imread(img)
                        video.write(write_img)
                    video.release()
                    print("next...")
                    shutil.rmtree("dataset_movie/temp_img/")
                    os.mkdir("dataset_movie/temp_img/")
            shutil.rmtree("dataset_movie/temp_img/")
            os.mkdir("dataset_movie/temp_img/")


if __name__ == '__main__':
    movie_dir = sys.argv[1]
    video_split(movie_dir)
