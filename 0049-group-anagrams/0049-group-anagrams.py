class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = defaultdict(list)
        
        for s in strs:
            charCount = [0] * 26
            
            for c in s:
                charCount[ord(c) - ord("a")] += 1
            
            anaDict[tuple(charCount)].append(s)     
        
        return anaDict.values()
        
            
        