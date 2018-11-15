import numpy as np
import cv2

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while(True):
    ret,frame=cap.read()
    cv2.imshow('frame',frame)

    k= cv2.waitKey(10) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
