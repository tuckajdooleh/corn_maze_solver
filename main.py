from Image import *
from Pathfinding import *
from Point import *

def main():

    image = Image("maze.jpg")
    pathfinding = Pathfinding(image)
    image.loadIMG()
    #decreasePathSize()
    pathfinding.createAllPossiblePaths(image.middlePoints,image.startPoint,image.endPoint)
    pathfinding.travelingSalesmanBruteForce(image.middlePoints, 0,{'path':[Point(image.startPoint[0],image.startPoint[1],None)],'length':0},image.startPoint,image.endPoint,{})
    pathfinding.drawResultPath(pathfinding.minimumPath,image)
    image.showImage()
        
main()