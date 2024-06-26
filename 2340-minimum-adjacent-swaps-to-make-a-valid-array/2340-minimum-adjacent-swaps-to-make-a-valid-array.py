class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        minEle = min(nums)
        maxEle = max(nums)
        minIndex, maxIndex = -1, 0
        
        for i in range(len(nums)):
            if nums[i] == minEle:
                minIndex = i
                break
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == maxEle:
                maxIndex = i
                break
                
        res = minIndex + (len(nums)-1-maxIndex)
        
        if minIndex > maxIndex:
            res -= 1
        
        return res
            
            