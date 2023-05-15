class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, maxLength = 0, 0, 0
        subSet = set() 
        
        while(r<len(s)):
            while (s[r] in subSet):
                subSet.remove(s[l])
                l += 1
            subSet.add(s[r])
            maxLength = max(maxLength, len(subSet))
            r += 1
        
        return maxLength
            
        '''
            if s[r] not in subSet:
                subSet.add(s[r])
            else:
                maxLength = max(maxLength, len(subSet))
                l += 1
                subSet = set(s[l])
                r = l
            r += 1
        
        return max(maxLength, len(subSet))
        '''