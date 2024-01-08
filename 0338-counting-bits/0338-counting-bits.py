class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        offset = 0
        currMul = 1
        
        for i in range(1, n+1):
            if i == currMul:
                offset = 0
                currMul *= 2
            res[i] = 1 + res[offset]    
            offset += 1
            
        return res