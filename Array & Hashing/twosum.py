def twoSum( nums, target):
    my_dict = {}
    for index,num in enumerate(nums):
        complement = target - num
        if complement in my_dict:
            return [my_dict[complement],index]
        my_dict[num] = index
    return []
     
nums = [4,5,6]
print(twoSum(nums,10))