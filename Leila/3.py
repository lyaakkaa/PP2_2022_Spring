N=int(input())
if N%2==1:
    for i in range(N):
        for j in range(N):
            if i>=j:
                print("#",end='')
            else:
                print(".",end="")
        print()
else:
    for i in range(N):
        for j in range(N):
            if i+j==N-1 or i+j>=N:
                print("#",end="")
            else:
                print(".",end="")
        print()