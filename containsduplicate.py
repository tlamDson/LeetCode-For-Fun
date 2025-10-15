class Solution(object):
    def containsDuplicate(self, nums):
        my_dict = {}
        for num in nums:
            if num in my_dict:
                return True
            my_dict[num] = True
        return False
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False
        #return len(nums) != len(set(nums))
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    
Solution().containsDuplicate([1,2,3,1])
       