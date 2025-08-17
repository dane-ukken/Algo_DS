class Solution:
    def simplifyPath(self, path: str) -> str:
        pathList = path.split('/')
        stack = []

        for p in pathList:
            if p == '.':
                continue
            if p == '..':
                if stack:
                    stack.pop()
                continue
            if p:
                stack.append(p)

        if not stack:
            return '/'
        return '/' + '/'.join(stack)

        