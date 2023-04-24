class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        i = 0
        j = len(s) - 1
        
        while (i<j and i<len(s) and j>=0) :
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
        
        '''
        newStr = ""
        
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1]
        '''
        
        
        """single pass"""
        """
        i = 0
        j = length - 1
        
        while (i<j and i<len(s) and j>=0) :
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
        """