class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        minEle = min(nums)
        maxEle = max(nums)
        minIndex, maxIndex = -1, 0
        
        for i in range(len(nums)):
            if minIndex == -1 and nums[i] == minEle:
                minIndex = i
            if nums[i] == maxEle:
                maxIndex = i

        res = minIndex + (len(nums)-1-maxIndex)
        
        if minIndex > maxIndex:
            res -= 1
        
        return res
            
            