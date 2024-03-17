class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        curr = 1
        for num in nums:
            if num-1 in numSet:
                continue
            curr = 0
            while num in numSet:
                num += 1
                curr += 1
            res = max(curr, res)
         
        return res
            
        
        
        