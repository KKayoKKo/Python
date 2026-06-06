class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.heigth = h

    def __str__(self):
        return str(self.x) + ", " + str(self.y) + ", " + str(self.width) + ", " + str(self.heigth)

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def setWidth(self, w):
        self.width = w

    def getWidth(self):
        return self.width

    def setHeigth(self, h):
        self.heigth = h

    def getHeigth(self):
        return self.heigth

    def getArea(self):
        return self.width * self.heigth

    def overlap(self, r):
        if self.x + self.width > r.x:
            if self.x < r.x + r.width:
                if self.y + self.heigth > r.y:
                    if self.y < r.y + r.heigth:
                        return True
        return False
    
#401p 4번 문제