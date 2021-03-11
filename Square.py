class Square:
    def __init__(self, side):
        self.side = side

    def getArea(self):
        return self.side ** 2

    def getPerimeter(self):
        return 4 * self.side
