class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pm = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    newPM = 4
                    if i>0 and grid[i-1][j]==1:
                        newPM -= 1
                    if i<m-1 and grid[i+1][j]==1:
                        newPM -= 1
                    if j>0 and grid[i][j-1]==1:
                        newPM -= 1
                    if j<n-1 and grid[i][j+1]==1:
                        newPM -= 1
                    pm += newPM
        return pm