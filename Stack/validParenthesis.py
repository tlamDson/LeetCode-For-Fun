class Solution(object):
    def isValid(s):
        if len(s) % 2 != 0:
            return False

        stack = []  
        mapping = {'(': ')', '[': ']', '{': '}'} 

        for char in s:
            if char in mapping:  
                stack.append(mapping[char])  
            else:  
                if not stack or stack.pop() != char:
                    return False

        return len(stack) == 0



