from picamera import PiCamera
import cv2

camera=PiCamera()
camera.resolution=(400,300)

camera.start_preview()

while True:
    k= cv2.waitKey(20) & 0xff
    if k==27:
        break

camera.stop_preview()
