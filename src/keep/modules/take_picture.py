import cv2
import os
import datetime


def take_user_picture(dir_path,user_id):
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.namedWindow('taking picture',cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("taking picture",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("taking picture",frame)
        cv2.moveWindow('taking picture', 0, 0)
        k = cv2.waitKey(1)

        if k == "27" or k == ord("q"):
            break
            cv2.destroyAllWindows()

        elif k == ord("s"):
            print("save img file.")
            dt_now = datetime.datetime.now()
            timestamp=dt_now.strftime('%Y%m%d')
            #print("type:{},{},{}".format(dir_path,timestamp,user_id))
            user_face_img = dir_path + timestamp +"_"+ str(user_id) + ".jpg"
            cv2.imwrite(user_face_img, frame)
            print("success.")
            cv2.destroyAllWindows()
            return user_face_img

if __name__ == '__main__':
    dir_path = "imgdata/"
    take_user_picture(dir_path,0)
