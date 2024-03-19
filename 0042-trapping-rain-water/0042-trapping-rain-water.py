class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        
        def getTrappedFromLeft(height):
            #print(height)
            nonlocal res
            l, r = 0, 0
            while l < len(height):
                r = l + 1
                blockArea = 0
                tallest = [0, 0]
                while r < len(height) and height[r] < height[l]:
                    blockArea += height[r]
                    if height[r] > height[r-1]:
                        tallest[0] = height[r]
                        tallest[1] = blockArea
                    r += 1
                if r == len(height):
                    return
                waterHeight = min(height[r], height[l])
                curr = waterHeight * (r - l)
                res += curr - blockArea - waterHeight
                l = r
        
        getTrappedFromLeft(height[:])
        maxHeight = max(height)
        newHeight = []
        i = len(height) - 1
        while i >= 0:
            newHeight.append(height[i])
            if height[i] == maxHeight:
                break
            i -= 1
        #print(newHeight)
        getTrappedFromLeft(newHeight[:])
        return res
            