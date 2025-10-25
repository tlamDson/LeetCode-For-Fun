def isValid( s):
    if len(s) % 2 != 0:
        return False
    stack = []
    mapping = {
        ')':'(',
        '}':'{',
        ']':'['}
    for c in s: 
        if c in mapping:
            # mapping[c] is the values
            if stack and stack[-1] == mapping[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False

    
           


        
print(isValid("([{}])"))       