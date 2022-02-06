to_dig= {'ZER': '0', 'ONE': '1', 'TWO': '2','THR': '3','FOU': '4','FIV': '5','SIX': '6','SEV': '7','EIG':'8', 'NIN':'9'}
to_let={v:k for k,v in to_dig.items()}

s = input().split('+')

k = []
for c in s:
    tmp = ''
    for i in range(0,len(c),3):
        tmp += to_dig[c[i:i+3]]
        a = tmp
    k.append(int(a))

ans = sum(k)
ans = str(ans)
z = ''
for c in ans:
    z += to_let[c]

print(z)
    
    
    
    