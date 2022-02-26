
def gen_sq(a,b):
    for i in range(a,b+1):
        yield i**2

a,b = map(int,input().split())
gen = gen_sq(a,b)
print(*[next(gen) for i in range(a,b+1)])
'''
gen_seq = (i**2 for i in range(1,n+1))
for i in gen_seq:
    print(i,end = ' ')
'''
    