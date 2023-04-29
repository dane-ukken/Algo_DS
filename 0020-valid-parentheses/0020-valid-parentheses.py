from queue import LifoQueue

class Solution:
    def isValid(self, s: str) -> bool:
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