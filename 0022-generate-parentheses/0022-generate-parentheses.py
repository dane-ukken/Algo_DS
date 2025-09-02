class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, o, close):
            if len(curr) >= 2 * n:
                if o == n and close == n:
                    res.append(''.join(curr))
                return
            
            curr.append('(')
            backtrack(curr[:], o + 1, close)
            curr.pop()
            if o > close:
                curr.append(')')
                backtrack(curr[:], o, close + 1)
        
        backtrack([], 0, 0)
        return res