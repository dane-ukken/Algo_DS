class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPals(l, r):
            count = 0
            while l >= 0 and r < len(s):
                if s[r] != s[l]:
                    break
                count += 1
                l -= 1
                r += 1
            
            return count
        
        res = 0
        for idx, c in enumerate(s):
            res += countPals(idx, idx)
            res += countPals(idx, idx+1)

        return res