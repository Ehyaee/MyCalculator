from math import pi


class Rectangle:
    def __init__(self, side1 , side2):
        self.side1 = side1
        self.side2 = side2

    def getArea(self):
        return self.side2* self.side1

    def getPerimeter(self):
        return 2*(self.side2+self.side1)
