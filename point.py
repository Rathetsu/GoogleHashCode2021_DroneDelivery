import math


class Point():

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def distance(self, target_point):
        dx = self.X - target_point.X
        dy = self.Y - target_point.Y
        return math.sqrt(dx**2 + dy**2)
