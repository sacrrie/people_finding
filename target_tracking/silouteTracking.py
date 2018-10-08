import sys
import cv2
import numpy as np

#read image
ir = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
#create rectangles from ir images
(T, trsh)=cv2.threshold(ir,150,255,cv2.THRESH_BINARY)
#cv2.imshow("First test",trsh)
mser=cv2.MSER_create()
regions= mser.detectRegions(trsh)
hulls=[cv2.convexHull(p.reshape(-1,1,2)) for p in regions[0]]
cv2.polylines(ir,hulls,1,(0,255,0))
cv2.imshow("mser",ir)
#record key press
k = cv2.waitKey(0)
