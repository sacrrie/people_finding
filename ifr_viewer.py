from functions import capture
import cv2
import numpy as np

while(True):
    frame=capture()
    frame=cv2.resize(frame,(0,0),fx=8,fy=8)
    cv2.imshow('thermal',frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
