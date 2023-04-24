class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        
        for i in range(len(nums)):
            if (target - nums[i]) in numDict.keys():
                return [i, numDict[(target - nums[i])]]
            numDict[nums[i]] = i
        
        return [-1, -1]