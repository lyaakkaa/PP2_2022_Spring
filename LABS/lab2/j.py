

import string

def proverka(s):
    d = False
    l = False
    u = False
    for c in s:
        if c in string.digits:
            d = True
    for c in s:
        if c in string.ascii_lowercase:
            l = True
    for c in s:
        if c in string.ascii_uppercase:
            u = True
    if d and l and u:
        return True
    return False

st = set()
for _ in range(int(input())):
    x = input()
    if proverka(x):
        st.add(x)
print(len(st))
for c in sorted(st):
    print(c)