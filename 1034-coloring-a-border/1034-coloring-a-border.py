class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        initialColor = grid[row][col]
        visited = set()
        
        def dfs(i, j):
            nonlocal initialColor
            if (i, j) in visited or i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != initialColor:
                return
            visited.add((i, j))
            isBorder = i == 0 or i == m - 1 or j == 0 or j == n - 1
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            if not isBorder:
                isBorder = (i - 1, j) not in visited or (i + 1, j) not in visited or (i, j - 1) not in visited or (i, j + 1) not in visited
            if isBorder:
                grid[i][j] = color
        
        dfs(row, col)
        return grid
