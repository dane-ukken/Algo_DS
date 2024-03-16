class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #(index, height)
        
        for i, h in enumerate(heights):
            curr = (i, h)
            while stack and stack[-1][1] >= h:
                curr = stack.pop()
                maxArea = max((i - curr[0])*curr[1], maxArea)
            stack.append((curr[0], h))
        
        while stack:
            curr = stack.pop()
            maxArea = max((len(heights) - curr[0])*curr[1], maxArea)
        
        return maxArea