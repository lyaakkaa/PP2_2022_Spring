import re
s = input()
pattern = r'[a-z]+_[a-z]+'
if re.search(pattern,s):
    print("Yes")
else:
    print("No")