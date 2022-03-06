import re

s = input()
#pattern = r'a.*?b$'
pattern = r'a[A-Za-z0-9]+b$'
if re.search(pattern,s):   # матч проверяет от начала строчки (начинается с а)
    print("Yes")
else:
    print("No")