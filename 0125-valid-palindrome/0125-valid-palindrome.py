class Solution:
    def isPalindrome(self, s: str) -> bool:
        """single pass"""
        length = len(s)
        i = 0
        j = length - 1
        
        while (i<j and i<length-1 and j>=0) :
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower()!=s[j].lower():
                return False
            else:
                i += 1
                j -= 1
                
        return True
        
        