class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countDict = {}
        
        for n in nums:
            if n in countDict:
                countDict[n] += 1
                return True
            else:
                countDict[n] = 1
        
        return False
        