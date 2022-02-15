

class Point:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def show(self):
        return f'point: ({self.a}, {self.b})' 
    
    def move(self,a,b):
        self.a = a
        self.b = b
        

    def dist(self,x):
        return ((self.a - x.a)**2 + (self.b - x.b)**2)**0.5

point1 = Point(1,3)
print(point1.show())
point2 = Point(2,2)
print(point1.dist(point2))

