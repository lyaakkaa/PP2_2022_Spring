


def proverka(num):
    if num == 1:
        return False
    elif num==0:
        return False
    for i in range(2,num//2):
        if num % i == 0:
            return False
    return True

a, b = map(int, input().split())
if proverka(a) and a<500 and b%2==0:
    print("Good job!")
else:
    print("Try next time!")
