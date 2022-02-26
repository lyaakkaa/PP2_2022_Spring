

def generator(n,k=1):
    for _ in range(n):
        yield k**2
        k+=1
n = int(input())
f = generator(n)
ans = [next(f) for _ in range(n)]
print(*ans)

