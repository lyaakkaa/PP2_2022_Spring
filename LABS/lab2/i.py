
polka = []
taken = []
for _ in range(int(input())):
    books = input().split()
    if books[0] == "1":
        polka.append(books[1])
    elif books[0]=='2':
        taken.append(polka[0])
        polka.pop(0)
for c in taken:
    print(c,end = " ")