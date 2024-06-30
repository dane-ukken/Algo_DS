class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        visited = set()
        m, n = len(isConnected), len(isConnected[0])
        
        def dfs(r, c):
            nonlocal m, n
            print(r,c)
            if (r, c) in visited or r < 0 or c < 0 or r == m or c == n:
                return 0
            
            visited.add((r, c))
            
            if isConnected[r][c] == 0:
                return 0
            
            for j in range(n):
                if isConnected[r][j] == 1 and (r, j) not in visited:
                    _ = dfs(j, r)
            visited.add((c, r))
            return 1
        
        for i in range(m):
            for j in range(n):
                #print(visited, i, j)
                if isConnected[i][j] == 1 and (i, j) not in visited:
                    res += dfs(i, j)
        
        return res