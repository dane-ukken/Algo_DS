class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlength, res, n = 0, "", len(s)
        
        def findLongestPalSubCenteredAtI(i):
            nonlocal maxlength, res, n, s
            l, r = i, i
            while (l >= 0) and (r<n) and (s[l] == s[r]):
                if (r-l+1 > maxlength):
                    res = s[l:r+1]
                    maxlength = r - l + 1
                l -= 1
                r += 1
        
        def findLongestPalSubCenteredAtIEven(i):
            nonlocal maxlength, res, n, s
            l, r = i, i+1
            while (l >= 0) and (r<n) and (s[l] == s[r]):
                if (r-l+1 > maxlength):
                    res = s[l:r+1]
                    maxlength = r - l + 1
                l -= 1
                r += 1
        
        for i in range(n):
            findLongestPalSubCenteredAtI(i)
            findLongestPalSubCenteredAtIEven(i)
        
        return res