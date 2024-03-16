class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #(index, height)
        
        for i, h in enumerate(heights):
            curr = (i, h)
            while stack and stack[-1][1] >= h:
                curr = stack.pop()
                currArea = (i - curr[0])*curr[1]
                if currArea > maxArea:
                    maxArea = currArea
            stack.append((curr[0], h))
        
        while stack:
            curr = stack.pop()
            currArea = (len(heights) - curr[0])*curr[1]
            if currArea > maxArea:
                    maxArea = currArea
        
        return maxArea