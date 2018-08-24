from pylepton import Lepton
import numpy as np
import cv2

def capture(device = "/dev/spidev0.0"):
    with Lepton(device) as l:
        f,_ = l.capture()
    cv2.normalize(f,f,0,65535,cv2.NORM_MINMAX)
    np.right_shift(f,8,f)
    return np.uint8(f)
#cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter('ifr_out.avi',fourcc,20.0,(80,60),False)

while(True):
    frame=capture()
    #frame = cv2.resize(frame,(0,0),fx=8,fy=8)
    out.write(frame)
    cv2.imshow('Thermal',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#cap.release()
out.release()
cv2.destroyAllWindows()
