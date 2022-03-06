import re

s = input()
pattern = r'(\w)([A-Z])'
new_pattern = r'\1_\2'
print(re.sub(pattern, new_pattern, s))