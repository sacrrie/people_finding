from pylepton import Lepton
import numpy as np
import cv2
from picamera import PiCamera

def capture(device = "/dev/spidev0.0"):
    with Lepton(device) as l:
        f,_ = l.capture()
    cv2.normalize(f,f,0,65535,cv2.NORM_MINMAX)
    np.right_shift(f,8,f)
    return np.uint8(f)
#cap = cv2.VideoCapture(0)
camera=PiCamera()
camera.resolution=(800,600)
fourcc = cv2.VideoWriter_fourcc(*'H264')
ifrout = cv2.VideoWriter('ifr_out.avi',fourcc,20.0,(80,60),False)
#rgbout = cv2.VideoWriter('rgb_out.avi',fourcc,20.0,(800,600),True)
camera.start_preview()
camera.start_recording('rgb_out.h264')

while(True):
    ifrframe=capture()
    #rgbframe=capture()
    #frame = cv2.resize(frame,(0,0),fx=8,fy=8)
    ifrout.write(ifrframe)
    cv2.imshow('Thermal',ifrframe)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#cap.release()
camera.stop_preview()
camera.stop_recording()
ifrout.release()
#rgbout.release()
cv2.destroyAllWindows()
