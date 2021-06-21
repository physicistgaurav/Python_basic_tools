#!/usr/bin/env python3
import cv2 
from datetime import datetime
time=datetime.now()
cam = cv2.VideoCapture(0)
ret, img = cam.read()
cv2.imshow("Test", img)
#print("Image "+str(time)+"saved")
file='/home/gaurav/Pictures/Okie/'+str(time)+'.jpg'
cv2.imwrite(file, img)

cam.release
cv2.destroyAllWindows
