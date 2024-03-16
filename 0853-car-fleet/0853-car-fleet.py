class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        time = {}
        res = 0    
        for i in range(n):
            x = position[i]
            time[x] = (target-x)/speed[i]        
        position.sort()
        while len(position) > 0:
            currTime = time[position.pop()]
            res += 1
            while len(position) > 0 and currTime >= time[position[-1]]:
                position.pop()
        return res