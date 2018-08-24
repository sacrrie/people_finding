from picamera import PiCamera
from time import sleep
import sys

camera = PiCamera()

camera.resolution=(800,600)
camera.start_preview()
camera.start_recording('/home/pi/Desktop/recodTestSmall.h264')
#camera.capture('/home/pi/Desktop/recodTestSmall.jpg')
#camera.resolution=(1280,720)
#camera.capture('/home/pi/Desktop/recodTestLarge.jpg')
#camera.resolution=(3280,2460)
#camera.capture('/home/pi/Desktop/recodTestSuperLarge.jpg')
#sleep(60)
camera.wait_recording(60)
camera.stop_recording()
camera.stop_preview()

