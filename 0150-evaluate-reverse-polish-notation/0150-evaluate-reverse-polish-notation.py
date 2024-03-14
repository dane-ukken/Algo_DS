class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        st = []
        for c in tokens:
            if c not in operators:
                st.append(c)
                continue
            res = nan
            b, a = int(st.pop()), int(st.pop())
            if c == '+':
                res = a + b
            elif c == '-':
                res = a - b
            elif c == '*':
                res = a * b
            elif c == '/':
                res = int(a / b)
            st.append(res)
                
        return int(st[0])
    