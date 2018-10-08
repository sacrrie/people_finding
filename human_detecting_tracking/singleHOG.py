from __future__ import print_function
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
#image = cv2.resize(image,(image.shape[1]*2,image.shape[0]*2))
orig = image.copy()

rv = hog.detect(image)
print(rv[0])
#(rects,weights) = hog.detectMultiScale(image)
cv2.waitKey(0)

