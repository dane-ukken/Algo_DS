class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = [] # pair: (index, val)
        
        for i, t in enumerate(temperatures):
            while len(stack) > 0 and t > stack[-1][1]:
                index, val = stack.pop()
                res[index] = i - index
            stack.append([i, t])
        return res
        
        '''
        res, stack = [0]*len(temperatures), []
        
        for i in range(len(temperatures)):
            j = 1
            while len(stack) > 0 and temperatures[i] > stack[-1]:
                while temperatures[i-j] != stack[-1]:
                    j += 1
                res[i-j] = j
                j += 1
                curr = stack.pop()
            stack.append(temperatures[i])
        
        return res
        '''            
        
        
        