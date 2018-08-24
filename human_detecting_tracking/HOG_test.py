from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

ap= argparse.ArgumentParser()
ap.add_argument("-i","--images",required = True, help="path to image file")
args=vars(ap.parse_args())

hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

image = cv2.imread(args["images"])
#image = image[120:235,170:310]
(a,b)=image.shape[1],image.shape[0]
image = cv2.resize(image,(image.shape[1]*2,image.shape[0]*2))
orig = image.copy()

(rects,weights) = hog.detectMultiScale(image,winStride=(3,3),padding=(4,4),scale=1.04)
#(rects,weights) = hog.detectMultiScale(image)
for (x,y,w,h) in rects:
    cv2.rectangle(orig,(x,y),(x+w,y+h),(0,0,255),2)
rects = np.array([[x,y,x+w,y+h] for (x,y,w,h)in rects])
pick = non_max_suppression(rects,probs=None,overlapThresh=0.65)

for (xA,yA,xB,yB) in pick:
    cv2.rectangle(image,(xA,yA),(xB,yB),(0,255,0),2)
print("{} original boxes,{} after suppression".format(len(rects),len(pick)))
image = cv2.resize(image,(a,b))
orig = cv2.resize(orig,(a,b))

cv2.imshow("With NMS",image)
cv2.imshow("Without NMS",orig)
cv2.waitKey(0)

