class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        winLen = len(s1)
        res = False
        if len(s2) < winLen:
            return res
        charCount = defaultdict(int)
        for c in s1:
            charCount[c] += 1
        l, r = 0, 0
        charDict = defaultdict(int)
        while r < len(s2):
            if s2[r] not in charCount:
                l, r = r+1, r+1
                charDict = defaultdict(int)
                continue
            charDict[s2[r]] += 1
            if r - l + 1 == winLen:
                if charDict == charCount:
                    return True
                charDict[s2[l]] -= 1
                if charDict[s2[l]] < 1:
                    charDict.pop(s2[l])
                l += 1
            r += 1
        return res