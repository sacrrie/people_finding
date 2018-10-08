#Too many overlapping bounding boxes, and non-max suppression isn't working
import sys
import cv2
import mahotas
import numpy as np
from imutils.object_detection import non_max_suppression


ir=cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)

simple=ir.copy()
threshold=ir.copy()
#mser=cv2.MSER_create(7,1000,10000,0.45,30,200,1.01,0.003,5)
mser=cv2.MSER_create()
mser.setPass2Only(True)
regions,_=mser.detectRegions(ir)
#non max suppression?
regions=np.array([[
    np.amin(p,axis=0)[0],
    np.amax(p,axis=0)[1],
    np.amax(p,axis=0)[0],
    np.amin(p,axis=0)[1]
    ] for p in regions] )
print("before")
print(len(regions))
picks = non_max_suppression(regions,probs=None,overlapThresh=0.35)
print("after")
print(len(picks))
for (xmin,ymax,xmax,ymin) in picks: #regions:
    #xmax,ymax= np.amax(p,axis=0)
    #xmin,ymin= np.amin(p,axis=0)
    cv2.rectangle(simple,(xmin,ymax),(xmax,ymin),(255,255,255),1)

simple=cv2.resize(simple,(0,0),fx=4,fy=4)
cv2.imshow("default RMSE",simple)
cv2.waitKey(0)

#there's no need to RMSE a binary image by definition
#MSER parametors explaination:
#delta
#this parameter indicates through how many different gray levels
#a region need to be stable to be considered maximally stable. For example,
#in a positive MSRE, the higher the pixel value it is the more likely it will 
#stay stable through multiple level of thresholds.
#In a word, higher the delta is, the lesser regions will be proposed(only those
#with high DN values will.

#min,maxArea
#as the names suggest, it regulates the size of the regions

#maxVariation
#same as delta, if a region is maximally stable, it can still be rejected if the 
#regions variation is bigger than the set value. For a smaller value, you get
#less regions

#minDiversity
# this parameter exists to prune regions that are too similar
#a higher value will get you a less number of regions
