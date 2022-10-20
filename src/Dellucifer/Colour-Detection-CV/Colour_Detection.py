# Importing OpenCV and NumPy Modules
import cv2
import numpy as np

def empty(x):
    pass

# Configuring the Frame 
frameWidth,frameHeight = 640,480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

# Configuring Windows
cv2.namedWindow('HSV')
cv2.resizeWindow('HSV',640,240)
cv2.createTrackbar("HUE min","HSV",0,255,empty)
cv2.createTrackbar("HUE max","HSV",179,255,empty)
cv2.createTrackbar("SAT min","HSV",0,255,empty)
cv2.createTrackbar("SAT max","HSV",255,255,empty)
cv2.createTrackbar("VALUE min","HSV",0,255,empty)
cv2.createTrackbar("VALUE max","HSV",255,255,empty)

# Code to Capture and perform Colour Detection
while True:
    success,img = cap.read()
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    cv2.imshow("Image", img)
    # cv2.imshow("HSV Image", img_hsv)

    h_min = cv2.getTrackbarPos("HUE min","HSV")
    h_max = cv2.getTrackbarPos("HUE max","HSV")
    s_min = cv2.getTrackbarPos("SAT min","HSV")
    s_max = cv2.getTrackbarPos("SAT max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE min","HSV")
    v_max = cv2.getTrackbarPos("VALUE max","HSV")

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(img_hsv,lower,upper)
    result = cv2.bitwise_and(img,img_hsv,mask = mask)

    cv2.imshow('mask',mask)
    cv2.imshow('result',result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Exiting the program
cap.release()
cv2.destroyWindow()
