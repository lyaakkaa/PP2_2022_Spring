def permute(a, left, right):
    if left==right:
        print(''.join(a))
    else:
        for i in range(left,right+1):
            a[left], a[i] = a[i], a[left]
            permute(a, left+1, right)
            a[left], a[i] = a[i], a[left] 

s = input()
permute(list(s), 0, len(s)-1)