import re
s = input()
pattern = r'ab{2,3}'
print(bool(re.search(pattern,s)))