class Solution:
    def romanToInt(self, s: str) -> int:
        
        romanVal = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        res = romanVal[s[0]]
        for i in range(1, len(s)):
            if romanVal[s[i]] > romanVal[s[i-1]]:
                res -= 2 * romanVal[s[i-1]]
            res += romanVal[s[i]]
        
        return res
            