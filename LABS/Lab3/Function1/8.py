# проверить есть ли 007 
def spy_game(nums):
    for i in range(len(nums)-2):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
    return False

nums = [int(i) for i in input().split()]
filter_num = list(filter(lambda x : x == 0 or x == 7,nums))

print(spy_game(filter_num))
        
