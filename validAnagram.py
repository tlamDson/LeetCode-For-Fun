class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS,countT= {},{}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
print(Solution().isAnagram('racecar','carrace'))
# class Solution(object):
#     def isAnagram(self, s, t):
#         if len(s) != len(t):
#             return False
        
#         count = {}
        
#         for i in range(len(s)):
#             count[s[i]] = count.get(s[i], 0) + 1
#             count[t[i]] = count.get(t[i], 0) - 1
        
#         # If all values are zero, then it's an anagram
#         return all(value == 0 for value in count.values())

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         count = [0] * 26
#         for i in range(len(s)):
#             count[ord(s[i]) - ord('a')] += 1
#             count[ord(t[i]) - ord('a')] -= 1

#         for val in count:
#             if val != 0:
#                 return False
#         return True
