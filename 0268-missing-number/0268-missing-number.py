class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        n, s = len(nums), 0
        
        for i in range(n):
            s += nums[i]
        
        return int(n*(n+1)/2 - s)
        
        """
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        
        return res
        """
        """