class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, maxLength = 0, 0, 0
        subSet = set() 
        n = len(s)
        
        while(r<n):
            if s[r] not in subSet:
                subSet.add(s[r])
            else:
                maxLength = max(maxLength, len(subSet))
                l += 1
                subSet = set(s[l])
                r = l
            r += 1
        
        return max(maxLength, len(subSet))