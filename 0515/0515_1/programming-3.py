class Box:
    def __init__(self, l, h, d):
        self.length = l
        self.height = h
        self.depth = d

    def __str__(self):
        return str(self.length) + ", " + str(self.height) + ", " + str(self.depth)

    def setLength(self, l):
        self.length = l

    def getLength(self):
        return self.length

    def setHeight(self, h):
        self.height = h

    def getHeight(self):
        return self.height

    def getDepth(self):
        return self.depth


b1 = Box(100, 100, 100)

print(b1)

volume = b1.getLength() * b1.getHeight() * b1.getDepth()
print("상자의 부피는", volume)

#401p 3번 문제