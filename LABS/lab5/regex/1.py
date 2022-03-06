import re

s = input()
pattern = r'ab*'

print(re.findall(pattern,s))