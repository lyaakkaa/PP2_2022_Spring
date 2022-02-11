
from math import sqrt

x, y = map(int,input().split())

def distance(numbers):
    dis = sqrt((x - numbers[0])**2 + (y - numbers[1])**2)
    return dis


points = []
n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    points.append((a,b))

ans = sorted(points,key=distance)
for i in ans:
    print(*i)



