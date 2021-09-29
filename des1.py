class Point:
    def __init__( self, x1=0, y1=0):
        self.x = x1
        self.y = y1
    def __del__(self):
        class_name = self.__class__.__name__
        print (class_name, "destroyed")
    def test(self):
        self.x=90
    def disp(self):
        print("x=",self.x,"y=",self.y)

pt1 = Point(100)
pt2 = pt1

pt2.disp()
pt2.test()

pt1.disp()
pt2.disp()
del pt1
del pt2
