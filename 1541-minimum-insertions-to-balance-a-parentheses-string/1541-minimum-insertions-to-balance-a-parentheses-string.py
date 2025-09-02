class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        st = []

        n = len(s)
        idx = 0
        while idx < n:
            if s[idx] == '(':
                st.append('(')
                idx += 1
            else:
                if idx == n - 1 or s[idx + 1] != ')':
                    res += 1
                    idx -= 1
                if not st:
                    res += 1
                else:
                    st.pop()
                idx += 2
        
        res += 2 * len(st)

        return res