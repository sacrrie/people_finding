from __future__ import print_function
from functions import FaceDetector
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True,
        help = "Path to the image")
args=vars(ap.parse_args())

#FaceCascade is hardcoded for now
fcPath="/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"

image = cv2.imread(args["image"])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
fd = FaceDetector(fcPath)
faceRects = fd.detect(gray, scaleFactor= 1.2)
print("{} face(s) found.".format(len(faceRects)))

for (x,y,w,h) in faceRects:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Faces",image)
cv2.waitKey(0)
