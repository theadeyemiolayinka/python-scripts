# Importing OpenCV and NumPy
import cv2
import numpy as np

circles = np.zeros((4,2),int)
counter = 0

# Defining Functions
def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(x, y)
        circles[counter] = x,y
        counter = counter + 1
        print(circles)

img = cv2.imread('cards.jpeg') # You can use image of your wish

# Loop to detect the clicks and crop the image
while True:
    if counter == 4:
        width, height = 250, 350
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        # print(pts1)
        pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        img_out = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow('Image_Output', img_out)

    for x in range(0, 4):
        cv2.circle(img, (int(circles[x][0]), int(circles[x][1])), 2, (0, 255, 0), cv2.FILLED)

    cv2.imshow('Image', img)
    cv2.setMouseCallback("Image", mousePoints)
    # print(circles)
    cv2.waitKey(1)

