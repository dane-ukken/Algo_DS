class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = "placeholder"
        n = len(nums)
        
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r)//2
            print(l, r, mid, nums[l], nums[r], nums[mid])
            prev = mid - 1
            #nxt = (mid + 1) % n
            if nums[prev] >= nums[mid]:
                return nums[mid]
            
            if nums[mid] < nums[r]:
                r = mid
                
            elif nums[mid] > nums[l]:
                l = mid
            else:
                l = mid + 1
        
        print("error")
        return -12345
            
            
        