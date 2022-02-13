#вывести со списка только простые
def proverka(num):
    if num == 1:
        return False
    elif num==0:
        return False
    for i in range(2,int(num**0.5 + 1)):
        if num % i == 0:
            return False
    return True

''''
def filter_prime(num):
    ans = []
    for c in num:
        if proverka(c):
            ans.append(c)
    return ans
'''  

num = [int(i) for i in input().split()]
filter_result = list(filter(lambda x: proverka(x), num))
print(filter_result)

'''print(filter_prime(num))'''