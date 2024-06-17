class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}
        
        def findWays(i, total):
            if i == len(nums):
                return 1 if total == target else 0
        
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = findWays(i+1, total+nums[i]) + findWays(i+1, total-nums[i])
            
            return dp[(i, total)]
    
        return findWays(0, 0)
        
        """
        Backtracking
        
        res = 0
        curr = 0
        n = len(nums)
        
        def findWays(i):
            nonlocal res, target, n, curr
            if i == n:
                if curr == target:
                    res += 1
                return
        
            curr += nums[i]
            findWays(i+1)
            curr -= nums[i]
            curr -= nums[i]
            findWays(i+1)
            curr += nums[i]
        
        findWays(0)
        return res
    
        """