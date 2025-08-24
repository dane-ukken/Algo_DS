class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)

        if ns > nt:
            return self.isOneEditDistance(t, s)

        if nt - ns > 1:
            return False

        for i in range(ns):
            if s[i] != t[i]:
                if ns == nt:
                    return s[i + 1 :] == t[i + 1 :]
                else:
                    return s[i:] == t[i + 1 :]
                    
        return ns + 1 == nt



        # edits = 0
        
        # if len(s) == len(t) - 1:
        #     if not t:
        #         return True
        #     idx = 0
        #     while idx < len(s):
        #         if edits > 1:
        #             return False
        #         if s[idx] != t[idx + edits]:
        #             edits += 1
        #         else:
        #             idx += 1
        
        # elif len(s) == len(t) + 1:
        #     if not s:
        #         return True
        #     idx = 0
        #     while idx < len(t):
        #         if edits > 1:
        #             return False
        #         if t[idx] != s[idx + edits]:
        #             edits += 1
        #         else:
        #             idx += 1
        
        # elif len(s) == len(t):
        #     for i in range(len(s)):
        #         if s[i] != t[i]:
        #             edits += 1
        #             if edits > 1:
        #                 return False
        #     if edits != 1:
        #         return False
        # else:
        #     return False
            
        # return True