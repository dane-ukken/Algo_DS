class Solution:
    def climbStairs(self, n: int) -> int:
        n2, n1 = 1, 1
        
        for i in range(1, n):
            n1, n2 = n2, n2+n1
        
        return n2
        