from functions import EyeTracker
import imutils
import argparse
import cv2

# This is face detecting in an video stream
ap = argparse.ArgumentParser()
# The face and eye cascade here is hard coded for now
#ap.add_argument("-f","--face",required = True),
#    help = "path to where the face cascade resides")
fcPath="/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
eyePath="/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml"

ap.add_argument("-v","--video",
        help = "Path to the optional video file")
args=vars(ap.parse_args())
et = EyeTracker(fcPath,eyePath)

if not args.get("video",False):
    camera = cv2.VideoCapture(0)
else:
    camera=cv2.VideoCapture(args["video"])

while True:
    (grabbed, frame)= camera.read()

    if args.get("video") and not grabbed:
        break

    frame = imutils.resize(frame,width=300)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = et.track(gray)
    for rect in rects:
        cv2.rectangle(frame,(rect[0],rect[1]),(rect[2],rect[3]),(0,255,0),2)

    cv2.imshow("Tracking",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
