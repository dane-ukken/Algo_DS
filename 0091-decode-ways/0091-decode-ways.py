class Solution:
    def numDecodings(self, s: str) -> int:
        codeDict = {"": 1}
        for i in range(26):
            if i+1 >= 11 and i+1 != 20:
                codeDict[str(i+1)] = 2
            else:
                codeDict[str(i+1)] = 1
        codeDict[""] = 0
                
        def findPossibleDecodeCount(s):
            nonlocal codeDict
            first, second = s[0:1], s[0:2]
            firstTotal, secondTotal = 0, 0
            if not s:
                return 0
            
            if s in codeDict:
                return codeDict[s]
            
            if first in codeDict:
                findPossibleDecodeCount(s[1:])
                firstTotal = codeDict[s[1:]]
            
            if second in codeDict and int(second) <= 26:
                findPossibleDecodeCount(s[2:])
                secondTotal = codeDict[s[2:]]
                        
            codeDict[s] = firstTotal + secondTotal
        
        findPossibleDecodeCount(s)
        return codeDict[s]
        
        