s = input()
x = input()
if x in s:
    print(s.find(x), end=' ') 
    if s.rfind(x) != s.find(x):
        print(s.rfind(x))