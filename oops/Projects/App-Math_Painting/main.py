from PIL import Image
from numpy import dtype



class Canvas:
    def __init__(self, height, width, color):
        self.color = color
        self.height = height
        self.width = width

        #create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width,3), dtype=np.uint8)

    def make(self):
        pass

class Rectangle:
    def __init__(self, x,y,a,b,color):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.color = color

    def draw(self, canvas):
        pass


class Square:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def draw(self, canvas):
        pass

canvas = Canvas(height=20, width=30, color=(255,255,255))
r1 = Rectangle(x=1,y=6, height=7,width=10,color=(100,200,125))
r1.draw(canvas)
s1=Square(x=1,y=3,side=3,color=(0,100,222))
s1.draw(canvas)
canvas.make('canvas.png')