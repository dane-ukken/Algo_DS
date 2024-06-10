class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        currSum = 0
        l, r = 0, 0
        
        while r < len(nums):
            while currSum < 0 and l < r:
                currSum -= nums[l]
                l += 1
            currSum += nums[r]
            res = max(currSum, res)
            r += 1
             
        return res