# grey scale frame reduce amount of data in matrices
import cv2
import time

video = cv2.VideoCapture(0)
time.sleep(1)
while True:
    check, frame = video.read()
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # guassian blur method, 21 is amount of blurness here and 0 is Standard deviation
    grey_frame_gau = cv2.GaussianBlur(grey_frame, (21, 21), 0)
    cv2.imshow("My video", grey_frame_gau)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break