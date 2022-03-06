import re

s = input()

pattern = r'(?=[A-Z])'
ls = re.split(pattern,s)
del ls[0]
print(*ls)