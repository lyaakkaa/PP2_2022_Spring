

dates = []
while True:
    dat = [i for i in input().split()]
    if dat[0] == '0':
        break
    else:
        d = dat[2] + ' ' + dat[1] + ' ' + dat[0]
        dates.append(d)


for c in sorted(dates):
    a = c.split()
    print(a[2],a[1],a[0])