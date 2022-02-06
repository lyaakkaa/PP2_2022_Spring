num = []
while True:
    x = int(input())
    if x == 0:
        break
    else:
        num.append(x)
ans = []
if len(num)%2==0:
    for i in range(len(num)//2):
        ans.append(num[i]+num[~i])
else:
    for i in range(len(num)//2 +1):
        ans.append(num[i]+num[~i])
    ans[-1]=ans[-1]//2

print(*ans)
    