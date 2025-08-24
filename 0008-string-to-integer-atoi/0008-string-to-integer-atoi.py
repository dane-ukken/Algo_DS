class Solution:
    def myAtoi(self, s: str) -> int:
        minVal, maxVal = -(2**31), 2**31 - 1
        hasStarted = False
        sign = 1
        res = 0
        
        for i in range(len(s)):
            c = s[i]
            if not hasStarted:
                if c in (' '):
                    continue
                    
                if c == '+':
                    hasStarted = True
                    continue
                    
                if c == '-':
                    sign = -1
                    hasStarted = True
                    continue
                
                if ord('0') <= ord(c) <= ord('9'):
                    hasStarted = True
                    res = res * 10 + int(c)
                    continue

            if ord('0') <= ord(c) <= ord('9'):
                res = res * 10 + int(c)
            else:
                break
            
            if res > maxVal:
                if sign == 1:
                    return maxVal
                else:
                    return minVal

        return res * sign