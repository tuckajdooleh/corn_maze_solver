from Point import *
from collections import deque
import sys

class Pathfinding:
    def __init__(self,image):
        self.points = []
        self.startPoint = []
        self.endPoint = []
        self.middlePoints = []
        self.allPossiblePaths = {}
        self.adjList = {}
        self.minimumPathLength = sys.maxsize
        self.minimumPath = []
        self.image = image

    def createAdjList(self):
        T = 200
        h = self.image.h
        w = self.image.w

        for y in range(0, h):
            for x in range(0, w):
                if(self.image.bw_img[y,x]>T):
                    currentPoint = Point(x,y,None)
                    
                    self.adjList[currentPoint.key] = []
                    
                    if x-1>0 and self.image.bw_img[y, x-1]>T:
                        self.adjList[currentPoint.key].append(Point(x-1,y,None))
                    if y-1>0 and self.image.bw_img[y-1, x]>T:
                        self.adjList[currentPoint.key].append(Point(x,y-1,None))
                    if x+1<w and self.image.bw_img[y, x+1]>T:
                        self.adjList[currentPoint.key].append(Point(x+1,y,None))
                    if y+1<h and self.image.bw_img[y+1, x]>T: 
                        self.adjList[currentPoint.key].append(Point(x,y+1,None))
        


    def BFS(self,start, end):
        q = deque()
        visited = {}

        q.append(start)

        visited[start.key] = True

        while len(q)>0:
            currentPoint = q.popleft()

            neighbors = self.adjList[currentPoint.key]

            for neighbor in neighbors:
                if neighbor.key not in visited:
                    if neighbor.key == end.key:
                        neighbor.parent = currentPoint
                        return neighbor    
                    neighbor.parent = currentPoint
                    visited[neighbor.key] = True
                    q.append(neighbor)
        return None

    def createPathFromEndNode(self,node):
        currentNode = node
        path = []
        while currentNode.parent is not None:
            path.append((currentNode.x,currentNode.y))
            currentNode = currentNode.parent
        return path

    def shortestPath(self,start, end):
        result = {'path':[] , 'length':0}
        self.createAdjList()
        node = self.BFS(Point(start[0],start[1],None),Point(end[0],end[1],None))
        path = self.createPathFromEndNode(node)
        result['path'] = path
        result['length'] = len(path)
        return result

    def createAllPossiblePaths(self,middle,start,end):
        
        for point in middle:#from start to all middle points
            fromKey = str(start[0]) + "," + str(start[1])
            toKey = str(point[0]) + "," + str(point[1])
            curPath = self.shortestPath(start,point)
            self.allPossiblePaths[fromKey+"-"+toKey] = curPath
            self.allPossiblePaths[toKey+"-"+fromKey] = curPath

        for point in middle:#from all points to the end point
            fromKey = str(point[0]) + "," + str(point[1])
            toKey = str(end[0]) + "," + str(end[1])
            curPath = self.shortestPath(point,end)
            self.allPossiblePaths[fromKey+"-"+toKey] = curPath
            self.allPossiblePaths[toKey+"-"+fromKey] = curPath

        for point in middle:#all middle points to all middle points
            for point2 in middle:
                if point is not point2:
                    fromKey = str(point[0]) + "," + str(point[1])
                    toKey = str(point2[0]) + "," + str(point2[1])
                    if fromKey+"-"+toKey not in self.allPossiblePaths and toKey+"-"+fromKey not in self.allPossiblePaths:
                        curPath = self.shortestPath(point,point2)
                        self.allPossiblePaths[fromKey+"-"+toKey] = curPath
                        self.allPossiblePaths[toKey+"-"+fromKey] = curPath

    def copyArray(self,points):          
        result = []
        for point in points:
            result.append(Point(point.x,point.y,None))
        return result

    def travelingSalesmanBruteForce(self,middle, index, currentPath,start,end,visited):

        if index >= len(middle):
            if currentPath['length'] < self.minimumPathLength:
                self.minimumPathLength = currentPath['length']
                self.minimumPath = self.copyArray(currentPath['path'])
        else:
            for i in range(len(middle)):
                curPoint = Point(middle[i][0],middle[i][1],None)
                prevPoint = currentPath['path'][index]
                if curPoint.key not in visited:
                    visited[curPoint.key] = True
                    currentPath['path'].append(curPoint)
                    curPathLength = self.allPossiblePaths[prevPoint.key+"-"+curPoint.key]['length']
                    currentPath['length']+=curPathLength
                    self.travelingSalesmanBruteForce(middle, index + 1, currentPath,start,end,visited)
                    del visited[curPoint.key]
                    currentPath['length']-=curPathLength
                    currentPath['path'].pop()

    def drawResultPath(self,result,image):
        lastPoint = result[0]
        for i in range(len(result)-1):
            curPoint = result[i+1]
            image.drawLine(self.allPossiblePaths[lastPoint.key+"-"+curPoint.key]['path'], image.img, image.randColor())
            lastPoint = curPoint