import random


s=input()
x=input()
ans = []
for i in range(len(s)):
    if s[i]==x:
        ans.append(i)
if len(ans)==1:
    print(ans[0])
else:
    print(ans[0],ans[-1])
