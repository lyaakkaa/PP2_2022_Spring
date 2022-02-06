


def proverka(args):
    pos = int(len(args) - 1)
    for i in range(len(args) - 2, -1, -1):
        if i + args[i] >= pos:
            pos = i
    if pos == 0:
        return True
    return False

jumps = [int(i) for i in input().split()]
if proverka(jumps):
    print(1)
else:
    print(0)