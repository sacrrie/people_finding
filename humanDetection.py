#version 0.0.1 alpha
#TODO: optimizing IFR frame chooser,HOG detector(multiScale -> singleScale)
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
from functions import *
from datetime import datetime
import time
import sys
print("Setting up...")
cv2.setUseOptimized(True)
cv2.setNumThreads(4)
pd=HOG_detector()
camera=PiCamera()
camera.resolution=(800,600)
camera.framerate=10
rawCaps= PiRGBArray(camera,size=(800,600))
fourcc= cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter('/home/pi/Videos/'+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'.avi',fourcc,10.0,(800,600),True)
time.sleep(0.5)
print("Done!")

for rawCap in camera.capture_continuous(rawCaps,format="bgr",use_video_port=True):
    rgb=rawCap.array
    ir=capture()
    thresh=threshold(ir)
    contours = find_ROI(thresh)
    for con in contours:
        con=trans_coordinate(con)
        con = enlarge(con)
        x,y,w,h=con
        parcel=rgb[y:y+h,x:x+w]
        #print("line 33")
        #cv2.waitKey(500)
        rects=pd.detectSingle(parcel)
        if len(rects)>0:
        #TODO Redraw the bounding box as it is
            for i in rects:
                cv2.rectangle(rgb,(x+i[0],y+i[1]),(x+i[0]+64,y+i[1]+128),(255,255,255),2,cv2.LINE_AA)
            cv2.rectangle(rgb,(x,y),(x+w,y+h),(0,255,255),2,cv2.LINE_AA)
        #debug purpose

        #for (X,Y,W,H) in rects:
        #    X=X+x;Y=Y+y
        #    cv2.rectangle(rgb,(X,Y),(X+W,Y+H),(255,255,255),2,cv2.LINE_AA)


        #cv2.rectangle(rgb,(x,y),(x+w,y+h),(255,255,255),2,cv2.LINE_AA)
    #ifr = resize(ifr)
    #cv2.imshow("bounding boxes ir",ifr)
    cv2.imshow("result",rgb)
    rawCaps.truncate(0)
    out.write(rgb)
    k= cv2.waitKey(30) & 0xff
    if k == 27:
        break
out.release()
cv2.destroyAllWindows()

