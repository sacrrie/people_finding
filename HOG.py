from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import imutils
import cv2

#def HOG_detect(images):

    #image = image[120:235,170:310]
    #(a,b)=image.shape[1],image.shape[0]
    #image = cv2.resize(image,(image.shape[1]*2,image.shape[0]*2))
    #for (x,y,w,h) in rects:
    #    cv2.rectangle(orig,(x,y),(x+w,y+h),(0,0,255),2)
    #image = cv2.resize(image,(a,b))
    #orig = cv2.resize(orig,(a,b))
class HOG_detector:
    def __init__(self):
        self.hog=cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def detect(self,image):
        #image = cv2.imread(images)
        (rects,weights) = self.hog.detectMultiScale(image,winStride=(8,8),padding=(8,8),scale=1.1)
        #(rects,weights) = self.hog.detect(image,winStride=(4,4))
        rects = np.array([[x,y,x+w,y+h] for (x,y,w,h)in rects])
        pick = non_max_suppression(rects,probs=None,overlapThresh=0.65)

        for (xA,yA,xB,yB) in pick:
            cv2.rectangle(image,(xA,yA),(xB,yB),(0,255,0),2)
        return image


