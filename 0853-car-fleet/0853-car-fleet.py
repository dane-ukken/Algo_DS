class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        pT = [(p, (target-p)/s) for p, s in zip(position,speed)]      
        pT.sort()
        while len(pT) > 0:
            currTime = (pT.pop())[1]
            res += 1
            while len(pT) > 0 and currTime >= (pT[-1])[1]:
                pT.pop()
        return res
        '''
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
        '''