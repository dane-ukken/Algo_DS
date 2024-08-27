class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 1 and val == nums[0]:
            return 0
        
        
        l, r = 0, n-1
        res = 0
        
        while l < r:
            while r >= 0 and nums[r] == val:
                res += 1
                r -= 1
            while l < n and nums[l] != val:
                l += 1

            if l < r:
                nums[r], nums[l] = nums[l], nums[r]

        return n-res