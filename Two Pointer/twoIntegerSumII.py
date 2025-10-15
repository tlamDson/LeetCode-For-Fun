def twoSum( numbers, target):
    left ,right = 0,len(numbers)-1

    while left <= right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [numbers[left],numbers[right]]
        elif current_sum < target:
            left +=1
        elif current_sum > target:
            right -=1
    return []
numbers = [0,1,2,3,4,5]
print(twoSum(numbers,3))