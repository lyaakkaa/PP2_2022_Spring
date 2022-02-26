


def generator(n):
    for i in range(n,-1,-1):
        yield i
n = int(input())
f = generator(n)
print(*[next(f) for _ in range(n,-1,-1)])

