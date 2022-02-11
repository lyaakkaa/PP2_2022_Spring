d = dict()
n = int(input())
for i in range(n):
    name, num = [i for i in input().split()]
    num = int(num)
    if name not in d:
        d[name] = num
    else:
        d[name] += num

maximum  = max(d.values())


for k in sorted(d):
    if d[k] == maximum:
        print(f"{k} is lucky!")
    else:
        print(f"{k} has to receive {maximum - d[k]} tenge")


