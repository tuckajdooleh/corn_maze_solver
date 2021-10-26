import cv2
#import numpy as np
#from numpy import array, arange, uint8 
#from matplotlib import pyplot as plt
h = 0
w = 0
img = None
bw_img = None

def loadIMG():
    global h
    global w
    global img
    global bw_img
    # read the image file
    img = cv2.imread('maze.jpg', cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, bw_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    # converting to its binary form
    bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # grab the image dimensions
    h = bw_img.shape[0]
    w = bw_img.shape[1]

def decreasePathSize():
    global h
    global w
    global img
    global bw_img

    tempImg = bw_img.copy()

    h = bw_img.shape[0]
    w = bw_img.shape[1]

    T = 200
    
    # loop over the bw_img, pixel by pixel
    for y in range(0, h):
        for x in range(0, w):
            # threshold the pixel
            if x-1>0 and tempImg[y, x-1]<T:
                bw_img[y, x] = 0
            if y-1>0 and tempImg[y-1, x]<T:
                bw_img[y, x] = 0
            if x+1<w and tempImg[y, x+1]<T:
                bw_img[y, x] = 0
            if y+1<h and tempImg[y+1, x]<T: 
                bw_img[y, x] = 0

loadIMG()
cv2.imshow("Binary", bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
decreasePathSize()
cv2.imshow("Binary", bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
