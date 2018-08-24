import sys
import cv2
import mahotas
import numpy as np

#read image
ir = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
cv2.imshow("original",ir)
#create thresholds
#thresh=cv2.adaptiveThreshold(ir,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,3)
back_up=ir.copy()
(T,trh)=cv2.threshold(back_up,150,255,cv2.THRESH_BINARY)
cv2.imshow("single value thresh",trh)
#otsu thresholding
print("otsu method")
T = mahotas.thresholding.otsu(ir)
thresh=ir.copy()
T=T+70
thresh[thresh>T]=255
thresh[thresh<T]=0
cv2.imshow("otsu thresh",thresh)

T2 = mahotas.thresholding.rc(ir)
thresh2=ir.copy()
T2=T2+70
thresh2[thresh2>T2]=255
thresh2[thresh2<T2]=0
cv2.imshow("riddler-calvard thresh",thresh2)

cv2.waitKey(0)
