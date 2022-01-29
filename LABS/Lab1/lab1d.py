num, x = int(input()), input()
if x=='k':
    c = int(input())
    print(round(num/1024, c))
else:
    print(num*1024)