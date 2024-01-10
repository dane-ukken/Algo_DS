class Solution:
    def reverse(self, x: int) -> int:
        digits = [-1] * 10
        isNeg = True if x < 0 else False
        iCount, currMul = 0, 1
        res = 0
        
        if isNeg:
            x *= -1
        
        for i in range(10):
            digits[i] = x % 10
            if x == 0:
                break
            x = x // 10
            iCount += 1
        
        for i in range(iCount-1, -1, -1):
            res += digits[i] * currMul
            currMul *= 10
        
        if isNeg:
            res *= -1
            
        if res < (-1)*2**(31) or res >= 2**31:
            return 0
        
        return res
            
        
        