def to_lower(s):
    a=''
    for c in s:
        if ord('A')<=ord(c)<=ord('Z'):
            a+=chr(ord(c)+32)
        else:
            a+=c
    return a
s=input()
print(to_lower(s))