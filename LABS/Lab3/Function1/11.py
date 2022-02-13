def chck_palindrom(s):
    a = s[::-1]
    if s == a:
        return True
    return False

print(chck_palindrom(input()))