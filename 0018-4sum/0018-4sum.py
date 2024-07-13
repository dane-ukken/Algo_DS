class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        a, b, c, d = 0, 1, n-2, n-1
        res = set()
        
        while a < n-3 :
            d = n-1
            while a < d-2:
                b = a + 1
                c = d - 1
                fl = False
                while b < c:
                    currSum = nums[a] + nums[b] + nums[c] + nums[d]

                    if currSum > target:
                        c -= 1
                    elif currSum < target:
                        b += 1
                    else:
                        res.add((nums[a], nums[b], nums[c], nums[d]))
                        fl
                        c -= 1
                        b += 1
            

                d -= 1

            a += 1
            
        return res