from movies import *
movies = moviess()

def chck5(mov,categ):
    ans = []
    for c in mov:
        if c['category'] == categ:
            ans.append(c['imdb'])
    return sum(ans)/len(ans)



print(chck5(movies,input()))