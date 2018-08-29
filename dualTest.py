import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
from functions import HOG_detector
import time
import sys
print("Setting up...")
cv2.setUseOptimized(True)
cv2.setNumThreads(4)
pd=HOG_detector()
camera=PiCamera()
camera.resolution=(800,600)
camera.framerate=24
rawCaps= PiRGBArray(camera,size=(800,600))
fourcc= cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter('sing_RGB.avi',fourcc,10.0,(800,600),True)
time.sleep(0.5)
print("Done!")

for rawCap in camera.capture_continuous(rawCaps,format="bgr",use_video_port=True):
    i=rawCap.array
    a=pd.detect(i)
    cv2.imshow("results",a)
    #cv2.imshow("results",i)
    rawCaps.truncate(0)
    out.write(a)
    k= cv2.waitKey(30) & 0xff
    if k == 27:
        break
out.release()
cv2.destroyAllWindows()

