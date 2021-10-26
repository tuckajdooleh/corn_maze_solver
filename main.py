import cv2
#import numpy as np
#from numpy import array, arange, uint8 
#from matplotlib import pyplot as plt
h = 0
w = 0
img = None
bw_img = None

points = []
startPoint = []
endPoint = []
middlePoints = []

adjList = {}#given a coordinate, return the list of all it's neighbors


# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):
    
    global points
    
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        '''cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
                    '''
        cv2.circle(img,(x,y),5,(255,0,0),-1)
        cv2.imshow('image', img)

        points.append((x,y))
 
    # checking for right mouse clicks    
    if event==cv2.EVENT_RBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)


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
def drawLine(points, img):
    for i in range(len(points)):
        img[points[i][1]][points[i][0]] = [0,0,255]

def createAdjList():
    global h
    global w
    global adjList
    global bw_img

    T = 200

    for y in range(0, h):
        for x in range(0, w):
            if(bw_img[y,x]>T):
                key = x + "," + y
                
                adjList[key] = []

                if x-1>0 and bw_img[y, x-1]>T:
                    adjList[key].append((x-1,y))
                if y-1>0 and bw_img[y-1, x]>T:
                    adjList[key].append((x,y-1))
                if x+1<w and bw_img[y, x+1]>T:
                    adjList[key].append((x+1,y))
                if y+1<h and bw_img[y+1, x]>T: 
                    adjList[key].append((x,y+1))
    
    
def BFS(start, end):
    global h
    global w
    global adjList
    global bw_img

    
    
def main():
    global startPoint
    global endPoint
    global points
    global middlePoints
    global img
    loadIMG()
    decreasePathSize()
    cv2.imshow("Binary", bw_img)
    cv2.setMouseCallback('Binary', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    startPoint = points[0];
    endPoint = points[-1];

    for i in range(len(points)-2):
        middlePoints.append(points[i+1])
    
    createAdjList()
    path = BFS(startPoint,endPoint)

    drawLine(path,img)

    cv2.imshow("Binary", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
main()