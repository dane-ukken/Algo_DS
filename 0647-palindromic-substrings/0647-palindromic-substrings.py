class Solution:
    def countSubstrings(self, s: str) -> int:
        palSubCount, n = 0, len(s)
        
        def addNumberOfPalSubCenteredAtI(i, evenVal):
            nonlocal n, s, palSubCount
            l, r = i, i+evenVal
            
            while l >= 0 and r < n and s[l]==s[r]:
                palSubCount += 1
                r += 1
                l -= 1
        
        for i in range(n):
            addNumberOfPalSubCenteredAtI(i, 0)
            addNumberOfPalSubCenteredAtI(i, 1)
        
        return palSubCount
        
        