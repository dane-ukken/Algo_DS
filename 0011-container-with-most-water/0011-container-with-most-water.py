class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            currArea = (r-l)*(min(height[r], height[l]))
            res = max(currArea, res)
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
                
        return res