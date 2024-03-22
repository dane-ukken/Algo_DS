class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            prev = mid - 1
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
            
            
        