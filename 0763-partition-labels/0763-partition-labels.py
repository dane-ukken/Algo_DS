class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charDict = {}
        n = len(s)
        
        for i in range(n):
            if s[i] not in charDict:
                charDict[s[i]] = [i, i]
            else:
                charDict[s[i]][1] = i
       
        res = []
        curr = []
        for i in range(n):
            c = s[i]
            if not curr:
                curr = charDict[c][:]
            if i == curr[1]:
                res.append(curr[1] - curr[0] + 1)
                curr = []
            else:
                curr[1] = max(curr[1], charDict[c][1])
        
        if curr:
            res.append(curr[1] - curr[0] + 1)
        
        
        return res