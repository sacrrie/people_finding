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
        (rects,weights) = self.hog.detectMultiScale(image,winStride=(4,4),scale=1.05)
        rects = np.array([[x,y,x+w,y+h] for (x,y,w,h)in rects])
        pick = non_max_suppression(rects,probs=None,overlapThresh=0.65)
        return pick

    def detectSingle(self,image):
        rects,_ = self.hog.detect(image)
        return rects

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

def find_ROI(image):
    _,contours,_=cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    boxes=[]
    for con in contours:
        if 25< cv2.contourArea(con) < 1000:
            boxes.append(cv2.boundingRect(con))
    return boxes

def resize(image):
    sized=cv2.resize(image,(0,0),fx=4,fy=4)
    return sized

def trans_coordinate(bounding_box):

    x,y,w,h = bounding_box
    #original parameter
    X=int(7.7*x+115)
    Y=int(8.5*y+45)
    W=int(7.7*w)
    H=int(8.5*h)
    
    return [X,Y,W,H]

#Temp enhance function
def enlarge(box):
    x,y,w,h=box
    x=x-20
    w=w+40
    y=y-20
    #TODO The processing of parameter h can cause strange behaviors
    #h=2*h
    h=2*h+40
    if x<0:
        x=0
    if y<0:
        y=0
    if (x+w)>800:
        w=800-x
    if (y+h)>600:
        h=600-y
    #print(x,y,w,h)
    return [x,y,w,h]
#Temp enhancement ends

