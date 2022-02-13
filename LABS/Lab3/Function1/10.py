# вывести уникальные без сета
def uni(ls):
    ans = []
    for c in ls:
        if c not in ans:
            ans.append(c)
    return ans

ls = [i for i in input().split()]
print(uni(ls))
