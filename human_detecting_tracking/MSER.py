import sys
import cv2
import mahotas
import numpy as np


ir=cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)

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
simple=ir.copy()
threshold=ir.copy()
mser=cv2.MSER_create()
regions,_=mser.detectRegions(ir)
for p in regions:
    xmax,ymax= np.amax(p,axis=0)
    xmin,ymin= np.amin(p,axis=0)
    cv2.rectangle(simple,(xmin,ymax),(xmax,ymin),(0,255,0),1)

cv2.imshow("default RMSE",simple)
#there's no need to RMSE a binary image by definition
cv2.waitKey(0)
