
import cv2 
import time 
import math

video = cv2.VideoCapture("bb3.mp4")
tracker = cv2.TrackerCSRT_create()
returned, img = video.read()
bbox = cv2.selectROI("rastreando",img,False)
tracker.init(img,bbox)
print(bbox)

def drawBox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img,"rastrando",(75,90),)