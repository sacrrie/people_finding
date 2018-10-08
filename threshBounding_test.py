import sys
import cv2
import numpy as np
import imutils
from functions import *


detector=HOG_detector()
ir = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
ifr=ir.copy()
rgb=cv2.imread(sys.argv[2])
thresh=threshold(ir)
contours=find_ROI(thresh)
for con in contours:
    con=trans_coordinate(con)
    con = enlarge(con)
    x,y,w,h=con
    parcel=rgb[y:y+h,x:x+w]
    rects=detector.detect(parcel)
    if len(rects)>0:
        cv2.rectangle(rgb,(x,y),(x+w,y+h),(255,255,255),2,cv2.LINE_AA)
cv2.imshow("bounding boxes",rgb)
cv2.waitKey(0)
