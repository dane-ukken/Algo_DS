class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        maxLength = 1
        currSet = set()
        currCount = defaultdict(lambda: 0)
        l, r = 0, 0
        
        while r < len(s):
            if s[r] not in currSet and len(currSet) >= 2:
                while len(currSet) >= 2:
                    currCount[s[l]] -= 1
                    if currCount[s[l]] == 0:
                        currSet.remove(s[l])
                    l += 1
            
            currSet.add(s[r])
            currCount[s[r]] += 1
            maxLength = max(maxLength, r-l+1)    
            r += 1
        
        return maxLength
        