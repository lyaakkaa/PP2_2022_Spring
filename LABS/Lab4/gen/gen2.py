

def generator(ans):
    for i in ans:
        if i % 2 == 0:
            yield i


n = int(input())
ans = [i for i in range(n+1)]
anss = []
for i in generator(ans):
    anss.append(i)

print(*anss,sep=',')