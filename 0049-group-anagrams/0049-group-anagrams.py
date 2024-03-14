class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = dict()
        
        for s in strs:
            t = ''.join(sorted(s))
            if t not in anaDict:
                anaDict[t] = []
            anaDict[t].append(s)
        
        return anaDict.values()
            
        