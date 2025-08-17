class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for p in path.split('/'):
            if not p or p == '.':
                continue
            if p == '..':
                if stack:
                    stack.pop()
                continue
            stack.append(p)

        return '/' + '/'.join(stack)

        