from picamera import PiCamera
import cv2

camera=PiCamera()
camera.resolution=(400,300)

camera.start_preview()

while True:
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

camera.stop_preview()
