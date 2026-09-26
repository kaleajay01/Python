class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def show(self):
        print(f"point(x:{self.x},y:{self.y})")

center=Point(45,56)
topleft=Point(77,99)
rightbottom=Point(96,12)

center.show()
topleft.show()
rightbottom.show()

