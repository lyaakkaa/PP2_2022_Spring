class res:
 
    def __init__(self, s):
        self.string = s   
 
    def printString(self):
        print(self.string.upper())
        

s = res(input())
s.printString() 