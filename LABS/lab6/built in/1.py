from functools import reduce
ls = [int(i) for i in input().split()]
print(reduce(lambda x,y: x * y,ls))
