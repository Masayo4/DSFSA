'''
カメラから映像を読み取って処理するスクリプト
主にテストようで使う
'''


import cv2
import dlib

detector = dlib.get_frontal_face_detector()
predictor_file_path = "models/shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_file_path)


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    dets = detector(frame[:, :, ::-1])
    if len(dets) > 0:
        parts = predictor(frame, dets[0]).parts()

        # 確認用 ---
        img = frame
        for i in parts:
            cv2.circle(img, (i.x, i.y), 3, (255, 0, 0), -1)

        cv2.imshow("me", img)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
