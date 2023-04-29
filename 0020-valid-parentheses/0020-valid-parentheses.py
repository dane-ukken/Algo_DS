#from queue import LifoQueue
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        bracketMap = {')': '(', ']': '[', '}': '{'}
        
        for c in s:
            if c in bracketMap.keys():
                if not bool(stack):
                    return False  
                if stack.pop() != bracketMap[c]:
                    return False
            else:
                stack.append(c)
        
        return True if not bool(stack) else False

        
        '''
        stack = LifoQueue()
        
        for c in s:
            if c in ('(', '[', '{'):
                stack.put(c)
                continue
            if stack.empty():
                return False
            a = stack.get()
            if c == ')':
                if a != '(':
                    return False
            if c == ']':
                if a != '[':
                    return False
            if c == '}':
                if a != '{':
                    return False
        
        return stack.empty()
        '''