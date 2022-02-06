

hunters = {}
demons = {}

for _ in range(int(input())):
    demon = [i for i in input().split()]
    demons[demon[1]] = demons.get(demon[1],0) + 1

for _ in range(int(input())):
    hunter = [i for i in input().split()]
    hunter[2]=int(hunter[2])
    if hunter[1] not in hunters:
        hunters[hunter[1]] = hunter[2]
    else:
        hunters[hunter[1]] += hunter[2]

ans = 0
for k in demons:
    if k in hunters:
        demons[k] = demons[k] - hunters[k]
    if demons[k] > 0:
        ans += demons[k]
print(f'Demons left: {ans}')


