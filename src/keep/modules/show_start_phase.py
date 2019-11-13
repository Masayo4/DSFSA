import cv2

def waiting_next():
    img_name = "../asset/background.jpeg"
    img = cv2.imread(img_name)
    #img = cv2.resize(img,(screen_width,screen_height))
    cv2.namedWindow('show_img',cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("show_img",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('show_img',img)
    cv2.moveWindow('show_img', 0, 0)
    k = cv2.waitKey(0)

    if k == "27" or k == ord("q"):
        cv2.destroyAllWindows()
    elif k == ord("n"):
        stage = 1
        print("nextstage...")
    #return stage

if __name__ == '__main__':
    #以下テスト用のコード
    #img_file_path = "../asset/system_architecture.png"
    window_fullscreen_manager(0)
