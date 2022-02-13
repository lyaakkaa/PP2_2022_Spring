from movies import *
movies = moviess()


def chck3(s):
    ans = []
    for c in movies:
        if c['category'] == s:
            ans.append(c['name'])

    return ans


print(chck3(input()))