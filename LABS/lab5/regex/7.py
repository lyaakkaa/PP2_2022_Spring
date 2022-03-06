import re
s = input()
a = s.capitalize()
ls = [c for c in a]
for i in range(len(ls)-1):
    if a[i] == '_':
        if a[i+1].islower():
            ls[i+1] = chr(ord(a[i+1])-32)
pattern = r'_'
print(re.sub(pattern,'',''.join(ls)))