from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
from pylepton import Lepton
import numpy as np
import imutils
import cv2

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

#def create_blob_detector(roi_size=(128, 128), blob_min_area=3, 
#                         blob_min_int=.5, blob_max_int=.95, blob_th_step=10):
#    params = cv2.SimpleBlobDetector_Params()
#    params.filterByArea = True
#    params.minArea = blob_min_area
#    params.maxArea = roi_size[0]*roi_size[1]
#    params.filterByCircularity = False
#    params.filterByColor = False
#    params.filterByConvexity = False
#    params.filterByInertia = False
#    # blob detection only works with "uint8" images.
#    params.minThreshold = int(blob_min_int*255)
#    params.maxThreshold = int(blob_max_int*255)
#    params.thresholdStep = blob_th_step
#    ver = (cv2.__version__).split('.')
#    if int(ver[0]) < 3:
#        return cv2.SimpleBlobDetector(params)
#    else:
#        return cv2.SimpleBlobDetector_create(params) 
