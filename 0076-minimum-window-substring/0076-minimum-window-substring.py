class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sCount = defaultdict(int)        
        tCount = defaultdict(int)
        res = [len(s), 0, ""]
        for x in t: tCount[x] += 1
        
        l, r = 0, 0
        need, have = len(tCount.keys()), 0
        while r < len(s):
            curr = s[r]
            if curr in tCount:
                sCount[curr] += 1
                if sCount[curr] == tCount[curr]:
                    have += 1

            while need == have:
                #print(res)
                if res[0] - res[1] + 1 > r - l + 1:
                    res = [r, l, s[l:r+1]]
                lCurr = s[l]
                if lCurr in tCount:
                    sCount[lCurr] -= 1
                    if sCount[lCurr] < tCount[lCurr]:
                        have -= 1
                l += 1
            r += 1

        return res[2]