class Shape:
    def get_area(self):
        return 0
class Rectangle(Shape):
    def __init__(self,len,wid):
        self.len = len
        self.wid = wid
        super().__init__()

    def get_Area(self):
        return self.len * self.wid

a, b = map(int,input().split())
rec1 = Rectangle(a,b)
print(rec1.get_Area())