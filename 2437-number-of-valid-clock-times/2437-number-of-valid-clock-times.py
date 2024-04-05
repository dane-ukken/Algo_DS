class Solution:
    def countTime(self, time: str) -> int:
        res = 1
        possibleCount = {3: 6, 4: 10}
        
        if time[0] == '?' and time[1] == '?':
            res = 24
        elif time[0] == '?':
            if int(time[1]) > 3:
                res = 2
            else:
                res = 3
        elif time[1] == '?':
            if int(time[0]) == 2:
                res = 4
            else:
                res = 10
        
        for i in range(3, 5):
            if time[i] == '?':
                res *= possibleCount[i]
        
        return res