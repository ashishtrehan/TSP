import numpy as np

class Destination:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #Euclidean Distance Formula
    def distance(self, destination):
        xDis = abs(self.x - destination.x)
        yDis = abs(self.y - destination.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"