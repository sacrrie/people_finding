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
orig = image.copy()

rv = hog.detect(image)
print(rv[0])
for i in rv[0]:
    cv2.rectangle(orig,(i[0],i[1]),(i[0]+64,i[1]+128),(255,255,255),2,cv2.LINE_AA)
cv2.imshow("results",orig)
cv2.waitKey(0)

