import random
import cv2

class Image:
    def __init__(self, imagePath):
        self.imagePath = imagePath
        self.h = 0
        self.w = 0
        self.img = None
        self.bw_img = None
        self.selectedPoints = []
        self.startPoint = None
        self.endPoint = None
        self.middlePoints = []

    def click_event(self,event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            font = cv2.FONT_HERSHEY_SIMPLEX
            '''cv2.putText(img, str(x) + ',' +
                        str(y), (x,y), font,
                        1, (255, 0, 0), 2)
                        '''
            cv2.circle(self.img,(x,y),5,(255,0,0),-1)
            cv2.imshow('image', self.img)
            self.selectedPoints.append((x,y))
        if event==cv2.EVENT_RBUTTONDOWN:
            font = cv2.FONT_HERSHEY_SIMPLEX
            b = self.img[y, x, 0]
            g = self.img[y, x, 1]
            r = self.img[y, x, 2]
            cv2.putText(self.img, str(b) + ',' +
                        str(g) + ',' + str(r),
                        (x,y), font, 1,
                        (255, 255, 0), 2)
            cv2.imshow('image', self.img)


    def loadIMG(self):
        self.img = cv2.imread(self.imagePath, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        ret, self.bw_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        bw = cv2.threshold(self.img, 127, 255, cv2.THRESH_BINARY)
        self.h = self.bw_img.shape[0]
        self.w = self.bw_img.shape[1]

        cv2.imshow("Binary", self.bw_img)
        cv2.setMouseCallback('Binary', self.click_event)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        self.startPoint = self.selectedPoints[0]
        self.endPoint = self.selectedPoints[-1]

        for i in range(len(self.selectedPoints)-2):
            self.middlePoints.append(self.selectedPoints[i+1])
        
    def decreasePathSize(self):
        
        tempImg = self.bw_img.copy()

        self.h = bw_img.shape[0]
        self.w = bw_img.shape[1]

        T = 200
        
        for y in range(0, h):
            for x in range(0, w):
                if x-1>0 and tempImg[y, x-1]<T:
                    self.bw_img[y, x] = 0
                if y-1>0 and tempImg[y-1, x]<T:
                    self.bw_img[y, x] = 0
                if x+1<w and tempImg[y, x+1]<T:
                    self.bw_img[y, x] = 0
                if y+1<h and tempImg[y+1, x]<T: 
                    self.bw_img[y, x] = 0
    def drawLine(self,points, img,color):
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            cv2.circle(img,(x,y),2,color,-1)

    def randColor(self):
        r = random.randrange(0, 255, 1)
        b = random.randrange(0, 255, 1)
        g = random.randrange(0, 255, 1)
        return (r,b,g)

    def showImage(self):
        cv2.imshow("Binary", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


