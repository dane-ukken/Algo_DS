class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                addendum = 0
                if i < m - 1:
                    addendum = grid[i + 1][j]
                if j < n - 1:
                    addendum = grid[i][j + 1]
                if i < m - 1 and j < n - 1:
                    addendum = min(grid[i + 1][j], grid[i][j + 1])
                grid[i][j] += addendum


        return grid[0][0]