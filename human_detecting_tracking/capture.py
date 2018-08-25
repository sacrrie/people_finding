from picamera import PiCamera
import time
camera=PiCamera()
camera.resolution=(800,600)
camera.start_preview()
i=0
while (i<10):
   print("capturing")
   camera.capture('/home/pi/test'+str(i)+'.jpg')
   time.sleep(5)
   i=i+1
camera.stop_preview()

