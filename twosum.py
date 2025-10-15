def twoSum(nums,target):
    my_dict = {}
    for index,num in enumerate(nums):
        complement = target - num
        if (complement in my_dict):
            return [my_dict[complement],index]
        my_dict[num] = index
        print(my_dict)
        return []
