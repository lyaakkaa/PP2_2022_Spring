
import string 

def check(s):
    big = string.ascii_uppercase
    small = string.ascii_lowercase
    num = string.digits
    b = False
    sm = False
    d = False
    for letter in s:
        if letter in big:
            b = True
        elif letter in small:
            sm = True
        elif letter in num:
            d = True
    if b == True and sm == True and d == True:
        return True
    return False 
ans = set()
n = int(input())
for i in range(n):
    s = input()
    if check(s) == True:
        ans.add(s)
print(len(ans))
anss = sorted(ans)
print(*anss,sep='\n')

    
