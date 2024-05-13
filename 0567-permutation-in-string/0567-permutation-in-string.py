class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        winLen = len(s1)
        res = False
        if len(s2) < winLen:
            return res
        charCount = Counter(s1)
        l, r = 0, 0
        charDict = defaultdict(lambda: 0)
        while r < len(s2):
            if s2[r] not in charCount:
                l, r = r+1, r+1
                charDict = defaultdict(lambda: 0)
                continue
            charDict[s2[r]] += 1
            if r - l + 1 == winLen:
                flag = True
                for key in charCount.keys():
                    if charCount[key] != charDict[key]:
                        flag = False
                if flag:
                    return True
                charDict[s2[l]] -= 1
                l += 1
            r += 1
        return res