class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1
        
        for n in nums:
            temp1 = currMax*n
            temp2 = currMin*n
            currMax = max(temp1, temp2, n)
            currMin = min(temp1, temp2, n)
            res = max(res, currMax)
        
        return res
        
        