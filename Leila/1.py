
shelf = []
taken = []

n = int(input())
for _ in range(n):
    z = [i for i in input().split()]
    if z[0] == '1':
        shelf.append(z[1])
    elif z[0] == '2':
        taken.append(shelf[0])
        del shelf[0] 

for i in taken:
    print(i,end=' ')