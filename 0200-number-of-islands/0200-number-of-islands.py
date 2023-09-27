class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0
        
        if not grid or not grid[0]:
            return islandCount
        
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if grid[i][j] == '1':
                grid[i][j] = 'v'
                if(i>0):
                    dfs(i-1, j)
                if(i<m-1):
                    dfs(i+1, j)
                if(j>0):
                    dfs(i, j-1)
                if(j<n-1):
                    dfs(i, j+1)
            else:
                return
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islandCount += 1
                    dfs(i, j)

        return islandCount