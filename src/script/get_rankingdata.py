import cv2
import os
import sys
import shutil
import datetime
import glob
from time import sleep
import dlib

def get_rankingdata(video_list):
    rankingdata = []
    predictor_path = "../dataset/models/shape_predictor_68_face_landmarks.dat"
    predictor = dlib.shape_predictor(predictor_path)
    detector = dlib.get_frontal_face_detector()
    #file_path = '../data/output_video/smile_video20191117210526.mp4'
    file_dir = video_list
    user_id = 1
    x = 0
    y = 0
    x_y_flag =0
    for file_path in file_dir:
        cap = cv2.VideoCapture(file_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                dets = detector(frame[:, :, ::-1])
                if len(dets) > 0:
                    parts = predictor(frame, dets[0]).parts()
                    img = frame * 0
                    for i in parts:
                        cv2.circle(img, (i.x, i.y), 3, (0, 255, 255), -1)
                    window_name = "user_" + str(user_id)
                    sleep(1/25)
                    cv2.imshow(window_name, img)
                    print(x)
                    cv2.moveWindow(window_name, x, y)
                    k = cv2.waitKey(5)
                    if k == "27" or k == ord("q"):
                        if x_y_flag == 0:
                            y = y +550;
                            x_y_flag = 1
                        elif x_y_flag == 1:
                            x = x +600
                            y = 0
                            x_y_flag = 0
                        break
            else:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        user_id = user_id +1

    cap.release()
    cv2.destroyAllWindows()

    typing_phase_img = "../asset/background.jpeg"
    img = cv2.imread(typing_phase_img)
    cv2.namedWindow('input_phase', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("input_phase",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("input_phase", img)
    cv2.moveWindow('show_img', 0, 0)
    while True:
        k = cv2.waitKey(0)

        if k == "27" or k == ord("q"):
            break
            cv2.destroyAllWindows()
        elif k == ord("1"):
            if rankingdata.count(1) == 0:
                rankingdata.append(1)
        elif k == ord("2"):
            if rankingdata.count(2) == 0:
                rankingdata.append(2)
        elif k == ord("3"):
            if rankingdata.count(3) == 0:
                rankingdata.append(3)
        elif k == ord("4"):
            if rankingdata.count(4) == 0:
                rankingdata.append(4)
        elif k == ord("5"):
            if rankingdata.count(5) == 0:
                rankingdata.append(5)
        elif k == ord("c"):
            rankingdata = []
        else:
            pass

        if len(rankingdata) == 5:
            break
    cv2.destroyAllWindows()
    return rankingdata


"""
        elif k == ord("1"):
            if rankingdata.count(1) == 0:
                rankingdata.append(1)
        elif k == ord("2"):
            if rankingdata.count(2) == 0:
                rankingdata.append(2)
        elif k == ord("3"):
            if rankingdata.count(3) == 0:
                rankingdata.append(3)
        elif k == ord("4"):
            if rankingdata.count(4) == 0:
                rankingdata.append(4)
        elif k == ord("5"):
            if rankingdata.count(5) == 0:
                rankingdata.append(5)
        elif k == ord("c"):
            rankingdata = []
        else:
            pass
        if len(rankingdata) == 5:
            break
"""





if __name__ == '__main__':
    difference = [0.22893946485260774, 0.08033175510204053, 0.03855379000141717, 0.0]
    video_list = ['../data/output_video/smile_video20191117195306.mp4',
    '../data/output_video/smile_video20191117195353.mp4',
    '../data/output_video/smile_video20191117195415.mp4',
    '../data/output_video/smile_video20191117210526.mp4']
    rankingdata = get_rankingdata(difference,video_list)
    print(rankingdata)
