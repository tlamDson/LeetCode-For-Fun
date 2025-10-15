def countString(nums):
    string_s = {}
    for index, num in enumerate(nums):
        if num in string_s:
            return True
        string_s[num] = index
    print(string_s)
    return False
countString([0,1,2,3,4])
       
 
