from movies import *
movies = moviess()

def chck2():
    ans = []
    for c in movies:
        if c['imdb'] > 5.5:
            ans.append(c['name'])
    return ans


print(chck2())