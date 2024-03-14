class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #operators = ['+', '-', '*', '/']
        stack = []
        operators = set(['+', '-', '*', '/'])

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                # Pop the last two numbers from the stack
                b, a = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Use int() for division to truncate towards zero
                    stack.append(int(a / b))
        
        return stack[0]
            