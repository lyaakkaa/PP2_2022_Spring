
b = []
for x in input():
    if x == "(" or x == "{" or x == "[":
        b.append(x)
    else:
        if len(b) == 0:
            print("No")
            quit()
        if x == ")" and b[-1] == "(":
            b.pop(-1)
        if x == "}" and b[-1] == "{":
            b.pop(-1)
        if x == "]" and b[-1] == "[":
            b.pop(-1)

if len(b) == 0:
    print("Yes")
else:
    print("No")