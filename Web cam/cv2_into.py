import cv2
import time
video = cv2.VideoCapture(0)
#
# time.sleep(1)
# check, frame = video.read()
# print(check, frame)
#
# time.sleep(1)
# check2, frame2 = video.read()
# print(check2, frame2)

# we can do better by while loop

time.sleep(1)
while True:
    check, frame = video.read()
    cv2.imshow("My video", frame)

    # key to close window
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
video.release()