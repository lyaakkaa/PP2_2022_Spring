def gr_to_unc(num):
    return num * 28.3495231

def Far_to_C(num):
    return (5/9)*(num-32)


def chicken_and_rabbits(heads,legs):
    for i in range(heads):
        for j in range(heads):
            if i + j == heads and 2*i + 4*j == legs:
                return i,j

def proverka(num):
    if num == 1:
        return False
    elif num==0:
        return False
    for i in range(2,int(num**0.5 + 1)):
        if num % i == 0:
            return False
    return True


def reverss(words):
    return words[::-1]


def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

def spy_game(nums):
    for i in range(len(nums)-2):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
    return False

def permute(a, left, right):
    if left==right:
        print(''.join(a))
    else:
        for i in range(left,right+1):
            a[left], a[i] = a[i], a[left]
            permute(a, left+1, right)
            a[left], a[i] = a[i], a[left] 

from math import pi


def volume(r):
    return 4*pi*r**3/3

def uni(ls):
    ans = []
    for c in ls:
        if c not in ans:
            ans.append(c)
    return ans


def chck_palindrom(s):
    a = s[::-1]
    if s == a:
        return True
    return False


def histogram(nums):
    ans = []
    for c in nums:
        ans.append('*'*c)
    return ans

import random
def guess():
    print('Hello! What is your name?')
    name = input()
    print()
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    num = random.randint(1, 20)
    print("Take a guess.")
    input_num = int(input())
    count = 0

    while input_num != num:
        if input_num > num:
            count += 1
            print()
            print('Your guess is too high')
            print("Take a guess.")
            input_num = int(input())
            continue
        elif input_num < num:
            count += 1
            print()
            print('Your guess is too low')
            print("Take a guess.")
            input_num = int(input())
            continue
    else:
        print(f'Good job, {name}! You guessed my number in {count+1} guesses!')

