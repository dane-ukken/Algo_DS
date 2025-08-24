class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        edits = 0
        
        if len(s) == len(t) - 1:
            if not t:
                return True
            idx = 0
            while idx < len(s):
                if edits > 1:
                    return False
                if s[idx] != t[idx + edits]:
                    edits += 1
                else:
                    idx += 1
        
        elif len(s) == len(t) + 1:
            if not s:
                return True
            idx = 0
            while idx < len(t):
                if edits > 1:
                    return False
                if t[idx] != s[idx + edits]:
                    edits += 1
                else:
                    idx += 1
        
        elif len(s) == len(t):
            for i in range(len(s)):
                if s[i] != t[i]:
                    edits += 1
                    if edits > 1:
                        return False
            if edits != 1:
                return False
        else:
            return False
            
        return True