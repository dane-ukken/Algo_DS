class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, res = 0, 0, 0

        while r < len(s):
            while s[r] in s[l:r]:
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res