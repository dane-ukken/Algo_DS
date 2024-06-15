class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for c in s:
            if c == ')':
                leftMax -= 1
                leftMin -= 1
            elif c == '(':
                leftMax += 1
                leftMin += 1
            else:
                leftMax += 1
                leftMin -= 1
            
            if leftMax < 0:
                return False
            
            leftMin = max(leftMin, 0)

        return True if leftMin == 0 else False
        
        """
        l, r, a = collections.deque(), collections.deque(), collections.deque()
        
        for i, c in enumerate(s):
            if c == ')':
                r.append(i)
            elif c == '(':
                l.append(i)
            else:
                a.append(i)
        
        count = 0
        curr = 0
        while l or r:
            if count < 0:
                if a and a[0] < curr:
                    count += 1
                    a.pop()
                else:
                    return False
            
            if not l or (l and r) and (r[0] < l[0]):
                curr = r.popleft()
                count -= 1
            
            elif not r or (l and r) and (l[0] < r[0]):
                curr = l.pop()
                count += 1
                 
        if abs(count) > len(a):
            while l and a and a[0] > l[-1]:
                l.pop()
                a.popleft()
                count -= 1
                
        else:
            while count < 0:
                
        
        return True
        
        """