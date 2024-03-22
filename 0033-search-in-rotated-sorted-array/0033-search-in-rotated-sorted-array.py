class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        ind = 0
        while l <= r:
            if nums[l] <= nums[r]:
                if nums[ind] > nums[l]:
                    ind = l
                break
            m = (l+r)//2
            if nums[ind] > nums[m]:
                ind = m
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        def findNum(l, r):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        
        if target >= nums[0]:
            return findNum(0, (n + ind-1) % n )
        else:
            return findNum(ind, n - 1)
    
        
        
        
        