n = int(input())
if n%2==0:
    mult = [['.'] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i>=j:
                mult[i][j]='#'
    for i in range(n):
        for j in range(n):
            print(mult[i][j],end='')
        print()
else:
    mult = [['.'] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i+j==n-1 or i+j>=n:
                mult[i][j]='#'
    for i in range(n):
        for j in range(n):
            print(mult[i][j],end='')
        print()
