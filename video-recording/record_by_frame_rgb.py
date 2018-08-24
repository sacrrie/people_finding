from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2
import time

camera=PiCamera()
camera.resolution=(800,600)
camera.framerate=32
rawCaptures = PiRGBArray(camera,size=(800,600))

time.sleep(0.2)

for rawCapture in camera.capture_continuous(rawCaptures,format="bgr",use_video_port=True):
    image = rawCapture.array
    cv2.imshow("Image",image)

    rawCaptures.truncate(0)
    k= cv2.waitKey(20) & 0xff
    if k==27:
        break

cv2.destroyAllWindows()
