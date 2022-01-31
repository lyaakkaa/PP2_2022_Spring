'''
def bin(n):
    b = ''
    while n > 0:
        b += str(n % 2) 
        n = n // 2
    return b[::-1]
'''
def to_dec(num):
    num = num[::-1]
    sum = 0
    for i in range(len(num)):
        sum+=int(num[i])*(2**i)

    return sum
'''
def to_dec_by_rec(num):
    if num == 0:
        return 0
    return num % 10 + 2 * to_dec_by_rec(num // 10)
'''

n = input()
print(to_dec(n))
