class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islandArea = [0]
        maxIslandArea = 0
        
        if not grid or not grid[0]:
            return islandCount
        
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if grid[i][j] == 1:
                grid[i][j] = 5
                islandArea[0] += 1
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
                if grid[i][j] == 1:
                    islandArea[0] = 0
                    dfs(i, j)
                    maxIslandArea = max(islandArea[0], maxIslandArea)

        return maxIslandArea