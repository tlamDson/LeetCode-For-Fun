def binarySearch(nums,target):
    for index,num in enumerate(nums):
        print(num,index)

        if num == target:
            return index
    return -1
        
nums = [-1,0,3,5,9,12]
binarySearch(nums,9)