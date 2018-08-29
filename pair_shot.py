from functions import capture
from datetime import datetime
import sys
import cv2
import numpy as np
import picamera

#usage: push s to shot, push q to quit
rgbcamera=picamera.PiCamera()
rgbcamera.resolution=(800,600)


while(True):
    frame=capture()
    orig=frame.copy()
    frame=cv2.resize(frame,(0,0),fx=8,fy=8)
    cv2.imshow('thermal',frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("/home/pi/test_shots/"+str(datetime.now())+"small.jpg",orig)
        cv2.imwrite("/home/pi/test_shots/"+str(datetime.now())+"large.jpg",frame)
        rgbcamera.capture("/home/pi/test_shots/"+str(datetime.now())+"color.jpg")
        print("pair photos shot")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
