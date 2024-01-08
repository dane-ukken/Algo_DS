class Solution:
    def reverseBits(self, n: int) -> int:
        res, currMul = 0, 1
        numArray = [0]*32
        
        for i in range(32):
            numArray[31 - i] = n % 2
            n = n // 2
        
        for i in range(32):
            res += numArray[i] * currMul
            currMul *= 2
        
        return res
        
            
            
            