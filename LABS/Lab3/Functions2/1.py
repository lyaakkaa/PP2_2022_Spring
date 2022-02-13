from movies import *
movies = moviess()


def chck1(s):
    for c in movies:
        if c['name'] == s:
            if c['imdb'] > 5.5 :
                return True

    return False


s = input()
print(chck1(s))