from functools import reduce
num = [int(i) for i in input().split()]
if len(num)==1:
    z = int(input())
    num.append(z)

arr = []
for i in range(num[0]):
    arr.append(num[1]+2*i)
ans = reduce(lambda x,y : x^y,arr,0)
print(ans)