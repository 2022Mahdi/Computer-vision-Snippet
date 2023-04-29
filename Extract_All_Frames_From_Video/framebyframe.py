import cv2
import os

path = ""
cap = cv2.VideoCapture(path)
count = 0
os.makedirs("Frames",exist_ok = True)

while cap.isOpened():
    ret,frame = cap.read()
    #cv2.imshow('window-name', frame)
    cv2.imwrite("Frames/frame%d.jpg" % count, frame)
    count = count + 1
    
print("resualt saved to Frames")
