class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) ==0):
            return 0
        
        r, l, maxLength, currLength = 0, 0, 0, 0
        
        while(r < len(s)):
            while(s[r] in s[l:r]):
                l += 1
                currLength -= 1
            currLength += 1
            if(currLength > maxLength):
                maxLength = currLength
            r += 1    
        return maxLength
              
               
            