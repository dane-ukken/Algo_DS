class Solution:
    def mySqrt(self, x: int) -> int:
        
        for i in range(x//2 + 2):
            sq = i * i
            
            if sq == x:
                return i
            
            if sq > x:
                return i - 1
