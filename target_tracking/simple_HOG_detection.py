#Try to adjust and tweak the detect() method to accelerate the speed
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
orig = image.copy()
#image=image[120:400,350:500]
#image = imutils.resize(image,width=64)
#(rects,weights) = hog.detectMultiScale(image,winStride=(6,6),scale=1.5)
#(rects,weights) = hog.detect(image)
rects,_ = hog.detect(image)
print(rects)
#for (x,y,w,h) in rects:
#    cv2.rectangle(orig,(x,y),(x+w,y+h),(0,0,255),2)
#rects = np.array([[x,y,x+w,y+h] for (x,y,w,h)in rects])
#pick = non_max_suppression(rects,probs=None,overlapThresh=0.65)

for (xA,yA,xB,yB) in rects:
    cv2.rectangle(image,(xA,yA),(xB,yB),(0,255,0),2)
#print("{} original boxes,{} after suppression".format(len(rects),len(pick)))

cv2.imshow("With NMS",image)
#cv2.imshow("Without NMS",orig)
cv2.waitKey(0)

