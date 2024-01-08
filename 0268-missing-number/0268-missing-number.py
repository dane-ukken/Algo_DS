class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n, s = len(nums), 0
        
        for i in range(n):
            s += nums[i]
        
        return int(n*(n+1)/2 - s)
        
        """
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ i 
            res = res ^ nums[i]
        
        res = res ^ len(nums)
        return res
        """