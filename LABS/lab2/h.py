
from math import sqrt
x, y = map(int,input().split())
def k(args):
    return (sqrt((x-args[0])**2+(y-args[1])**2))
num = []
for _ in range(int(input())):
    x1,y1 = map(int,input().split())
    num.append((x1,y1)) 
a= sorted(num,key=k)
for c in a:
    print(c[0],c[1])