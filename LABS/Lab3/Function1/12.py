def histogram(nums):
    ans = []
    for c in nums:
        ans.append('*'*c)
    return ans

num = [int(i) for i in input().split()]
print(*histogram(num),sep='\n')        