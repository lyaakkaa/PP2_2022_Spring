class Shape:
    def get_area(self):
        return 0

class Square(Shape):
    def __init__(self,len):
        self.len = len
    
    def get_area(self):
        return self.len ** 2

a = Square(int(input()))
print(a.get_area())


