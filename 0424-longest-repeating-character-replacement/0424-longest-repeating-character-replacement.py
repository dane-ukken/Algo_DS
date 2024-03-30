class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = 0
        res= 0 
        countDict = defaultdict(lambda: 0)
        
        l, r = 0, 0
        while r < len(s):
            countDict[s[r]] += 1
            maxF = max(maxF, countDict[s[r]])
            
            while r - l + 1 - maxF > k:
                countDict[s[l]] -= 1    
                l += 1
                
            res = max(r - l + 1, res)
            r += 1
                
        return res