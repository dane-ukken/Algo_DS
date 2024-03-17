class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res, pre, post = [1]*n, [1]*(n+2), [1]*(n+2)
        
        for i in range(n):
            pre[i+1] = pre[i]*nums[i]
            post[-2-i] = post[-1-i]*nums[-1-i]
        
        for i in range(n):
            res[i] = pre[i]*post[i+2]
        
        return res
        