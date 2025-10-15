def binarySearch(nums,target):
    # fisrt have the left and right bound
    left,right = 0, len(nums)-1
    #why right is len(nums) -1 but now len(nums) because the index starts at 0 so the last valid index is equal to the total length(included 0) minus 1
    #now we implement the core of the functions
    while left <= right:
        mid = (left + right) //2 # need to take the mod because we cannot compare a float to an int
        if nums[mid] == target:
            return mid # we return the index
        elif nums[mid] < target:
            left = mid + 1 # if nums[mid] < target it means that everything from the left is smaller than the value at mid so do not need to search for the value of mid
        else:
            right = mid -1
    return -1
numbers = [1, 3, 5, 7, 9, 11]
print(binarySearch(numbers,3))