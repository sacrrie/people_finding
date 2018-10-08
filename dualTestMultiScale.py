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
        #ratio=parcel.shape[0]/400.0
        #parcel=imutils.resize(parcel,height=400)
        rects=pd.detect(parcel)
        #for rect in rects:
        #    rect=rect*ratio
        #    (X,Y,W,H)=rect
        #    X=int(X);Y=int(Y);W=int(W);H=int(H);
        #    X=X+x;Y=Y+y
        #    cv2.rectangle(rgb,(X,Y),(X+W,Y+H),(255,255,255),2,cv2.LINE_AA)
        if len(rects)>0:
            cv2.rectangle(rgb,(x,y),(x+w,y+h),(255,255,255),2,cv2.LINE_AA)

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

