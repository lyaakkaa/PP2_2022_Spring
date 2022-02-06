
n = int(input())
mult = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i==0:
            mult[i][j]=j
        elif j==0:
            mult[i][j]=i
        elif i==j:
            mult[i][j] = i * j
for i in range(n):
    for j in range(n):
        print((mult[i][j]), end=' ')
    print()
