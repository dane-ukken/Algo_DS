class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        result.append([])
        
        for num in nums:
            result = self.addToResult(result, num)
        
        return result
            
    
    def addToResult(self, resultSet: List[List[int]], num: int) -> List[List[int]]:
        newSets = []
        for currentSet in resultSet:
            newSets.append(currentSet[:])
            currentSet.append(num)
            newSets.append(currentSet[:])
        return newSets