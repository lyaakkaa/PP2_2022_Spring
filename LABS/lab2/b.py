'''
n = int(input())
num = [int(i) for i in input().split()]
ans = []
for i in range(n):
    for j in range(n):
        if i!=j:
            ans.append(num[i]*num[j])
print(max(ans))

'''

n = int(input())
num = [int(i) for i in input().split()]
print(max([num[i]*num[j] for i in range(n) for j in range(n) if i!=j]))
