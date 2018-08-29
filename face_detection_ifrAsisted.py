#!/usr/bin/env python
'''
Usage:
        python3 face_detection_ifrAsisted.py input_image asist_ir_image
'''

import sys
import cv2
import math

if __name__=='__main__':
    #If image path and f/q is not passed as command
    #line arguments,quit and display help message
    if len(sys.argv) <3:
        print(__doc__)
        sys.exit(1)

    #Speed-up using multithreads
    cv2.setUseOptimized(True);
    cv2.setNumThreads(4);

    #read image
    im = cv2.imread(sys.argv[1])
    im_backup=im
    ir = cv2.imread(sys.argv[2])
    ratio=math.ceil(im.shape[1]/ir.shape[1])
    #resize image TODO:make it optional later
    #newHeight = 200
    #newWidth = int(im.shape[1]*newHeight/im.shape[0])
    #im = cv2.resize(im,(newWidth, newHeight))

     
    #face detection expects a gray scale image
    im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ir = cv2.cvtColor(ir,cv2.COLOR_BGR2GRAY)
    #create rectangles from ir images
    ret,ir1=cv2.threshold(ir,10,10,10)
    ir2,contours,hierarchy=cv2.findContours(ir1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   
    face_detector=cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

    while True:
        #create a copy of original image
        imOut= im_backup.copy()
        #itereate over all the region proposals
        for rect in contours:
            x,y,w,h = cv2.boundingRect(rect)#TODO: Does python support vectorized computing?
            x*=ratio
            y*=ratio
            w*=ratio
            h*=ratio
            parcel= im[y-25:y+h,x-50:x+w+50]
            cv2.imshow("parts",parcel)
            #TODO: Figure out the dimensions of the minSize parameter
            #faces= face_detector.detectMultiScale(parcel,minSize=(w-1,h-1),maxSize=(w-1,h-1))
            faces= face_detector.detectMultiScale(parcel,1.1,5)
            if(len(faces)>0):
                print("bingo")
                cv2.rectangle(imOut,(x,y),(x+w,y+h),(255,0,0),1, cv2.LINE_AA)
            else:
                cv2.rectangle(imOut,(x,y),(x+w, y+h),(0,255,0),1, cv2.LINE_AA)
        #show output
        cv2.imshow("Output",imOut)

        #record key press
        k = cv2.waitKey(0) & 0xFF

        #and process the key press
        if k==113: # q
            break
    #close image show window
    cv2.destroyAllWindows()


