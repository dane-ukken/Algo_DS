class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = nums[0]
        
        for i in range(1, len(nums)):
            res = res ^ i 
            res = res ^ nums[i]
        
        res = res ^ len(nums)
        return res