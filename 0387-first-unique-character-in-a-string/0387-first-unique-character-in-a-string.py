class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = set()
        idxList = [float('inf')] * 26

        for idx, c in enumerate(s):
            if c in chars:
                idxList[ord(c) - ord('a')] = float('inf')
            else:
                chars.add(c)
                idxList[ord(c) - ord('a')] = idx
        
        if min(idxList) == float('inf'):
            return -1
        
        return min(idxList)
        

