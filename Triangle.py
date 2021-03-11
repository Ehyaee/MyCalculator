class Triangle:
    def __init__(self, base , height , b, c):
        self.base = base
        self.height = height
        self.b = b
        self.c = c

    def getArea(self):
        return 1/2*self.base*self.height

    def getPerimeter(self):
        return self.base+self.b+self.c

