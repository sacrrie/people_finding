import cv2
import sys
from HOG import HOG_detector
pd=HOG_detector()

i= cv2.imread(sys.argv[1])
a=pd.detect(i)
cv2.imshow("result",a)
cv2.waitKey(0)


