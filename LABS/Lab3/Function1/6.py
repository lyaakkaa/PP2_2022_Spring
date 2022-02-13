#перевернуть список
def reverss(words):
    return words[::-1]

words = [i for i in input().split()]
print(*reverss(words))