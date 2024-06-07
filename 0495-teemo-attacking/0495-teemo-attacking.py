class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        resetTime = 0
        
        for t in timeSeries:
            res += duration
            if resetTime > t:
                res -= resetTime - t
            resetTime = t + duration
        
        return res