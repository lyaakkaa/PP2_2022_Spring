
import string
s = input()
z = string.punctuation
for c in s:
    if c in z:
        s = s.replace(c,'')

ans = set(s.split())
print(len(ans))
print(*sorted(ans),sep='\n')
