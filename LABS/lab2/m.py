

dates = []
while True:
    dat = input()
    if dat == '0':
        break
    else:
        dd,mm,yy = dat.split()
        dates.append((dd,mm,yy))


for c in sorted(dates,key = lambda x : (x[2],x[1],x[0])):
    print(*c)
