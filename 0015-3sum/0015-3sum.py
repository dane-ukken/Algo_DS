class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        
        i = 0
        while i < n:
            target = nums[i]
            #implement two sum
            l, r = i + 1, n - 1
            
            while l < r:
                curr = nums[l] + nums[r]
                if curr == -target:
                    res.append([target, nums[l], nums[r]])
                    l += 1
                    while l < n-1 and nums[l] == nums[l-1]:
                        l += 1
                elif curr > -target:
                    r -= 1
                else:
                    l += 1
                
            i += 1
            while i<n-1 and nums[i] == nums[i-1]:
                i += 1
        return res