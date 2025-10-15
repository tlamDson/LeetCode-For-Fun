def productExceptSelf(nums):
    #brute force solution
    # new_array = []
    # for i in range(len(nums)):
    #     copy_array = nums.copy()
    #     copy_array.pop(i)
    #     product = 1
    #     for num in copy_array:
    #         product = product*num
    #     new_array.append(product)
    # print(new_array)

    #ANOTHER USING PREFIX AND SUFFIX PROBLEM THIS IS REALLY INTERESTING I WILL EXPLAIN IT LATER
    n = len(nums)
    output = [1]*n

    p = 1
    for i in range(n):
      output[i] =p
      p*=nums[i]
    p = 1
    for i in range(n-1,-1,-1):
       output[i] *= p
       p*=nums[i]
    return output
    
numbers = [1,2,4,6]
productExceptSelf(numbers)
