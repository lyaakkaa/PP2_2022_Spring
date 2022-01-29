
def bin(n):
    b = ''
    while n > 0:
        b += str(n % 2) 
        n = n // 2
    return b[::-1]

def to_dec(num):
    num = num[::-1]
    sum = 0
    for i in range(len(num)):
        sum+=int(num[i])*(2**i)

    return sum

print(to_dec(input()))