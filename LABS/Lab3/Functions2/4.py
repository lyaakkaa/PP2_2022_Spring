from movies import *
movies = moviess()


def chck4(mov):
    ans = []
    for c in mov:
        ans.append(c['imdb'])
    return sum(ans)/len(ans)


print(chck4(movies))