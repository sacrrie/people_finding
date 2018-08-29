#no blob detection neither, doesn't work well, will just use find countours
import sys
import cv2
import numpy as np
from imutils.object_detection import non_max_suppression


ir=cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)

simple=ir.copy()
threshold=ir.copy()


params = cv2.SimpleBlobDetector_Params()
params.filterByColor=True
params.blobColor= 255
params.minThreshold = 110
params.maxThreshold = 225
params.filterByArea = True
params.minArea = 40
#params.maxArea = 250
params.filterByInertia = True
params.minInertiaRatio = 0.3
blob_detector = cv2.SimpleBlobDetector_create(params)
#blob_detector = cv2.SimpleBlobDetector_create()
kp = blob_detector.detect(ir)
print(kp)
im=cv2.drawKeypoints(ir,kp,np.array([]),(255,255,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


cv2.imshow("default blob detection",im)
cv2.waitKey(0)
#non max suppression?
#regions=np.array([[
#    np.amin(p,axis=0)[0],
#    np.amax(p,axis=0)[1],
#    np.amax(p,axis=0)[0],
#    np.amin(p,axis=0)[1]
#    ] for p in regions] )
#picks = non_max_suppression(regions,probs=None,overlapThresh=0.35)
#for (xmin,ymax,xmax,ymin) in picks: #regions:
#    #xmax,ymax= np.amax(p,axis=0)
#    #xmin,ymin= np.amin(p,axis=0)
#    cv2.rectangle(simple,(xmin,ymax),(xmax,ymin),(255,255,255),1)

