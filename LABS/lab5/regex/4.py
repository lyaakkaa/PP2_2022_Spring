import re

s = input()
pattern = r'[A-Z][a-z]+'
if re.search(pattern,s):
    print("Yes")
else:
    print("No")