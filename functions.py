from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
from pylepton import Lepton
import numpy as np
import imutils
import cv2
import mahotas

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

def capture(device = "/dev/spidev0.0"):
    with Lepton(device) as l:
        f,_ = l.capture()
    cv2.normalize(f,f,0,65535,cv2.NORM_MINMAX)
    np.right_shift(f,8,f)
    return np.uint8(f)

def threshold(image):
    T=mahotas.thresholding.rc(image)+40
    image[image>T]=255
    image[image<T]=0
    return image

