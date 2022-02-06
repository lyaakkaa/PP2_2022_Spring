d = {}
for _ in range(int(input())):
    name, num = [i for i in input().split()]
    num = int(num)
    if name not in d:
        d[name] = num
    else:
        d[name] +=num    

maxi = max(d.values())
for k in sorted(d):
    if d[k]==maxi:
        print(f'{k} is lucky!')
    else:
        print(f'{k} has to receive {maxi-d[k]} tenge')
