#подсчитать колво кур и кроликов

def chicken_and_rabbits(heads,legs):
    for i in range(heads):
        for j in range(heads):
            if i + j == heads and 2*i + 4*j == legs:
                return i,j

print(*chicken_and_rabbits(35,94))
