# two pointers so read the head and the tail of the string and then the head plus 1 and the tail plus 1
# if it an odd so check if the string is equal to the middle so have the middle of the string
# if it and even so still check for the middle 1st plus the last and the divided by 2
import re
def isPalindrome(s):
    s = re.sub(r'[^A-Za-z0-9 ]', '', s)  
    s = s.replace(" ", "").lower()
    start = 0
    end = -1
    middle = len(s) // 2
    while s[start] == s[end]:
        if start < middle:
            start+= 1
            end -=1
        return    
s ="abba"
isPalindrome(s)
