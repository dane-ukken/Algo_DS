class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        i, j = 0, len(s) - 1
        
        while (i<j) :
            if not self.isAlphaNum(s[i]):
                i += 1
                continue
            if not self.isAlphaNum(s[j]):
                j -= 1
                continue
            if s[i].lower()!=s[j].lower():
                return False
            i += 1
            j -= 1
                
        return True

    def isAlphaNum(self, c) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        
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
        j = len(s) - 1
        
        while (i<j) :
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