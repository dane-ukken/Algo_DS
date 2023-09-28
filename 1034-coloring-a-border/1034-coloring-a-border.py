class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        initialColor = grid[row][col]
        visitedColors = [initialColor, 0, -1]
        
        def dfs(i, j):
            nonlocal initialColor
            if grid[i][j] != initialColor:
                return
            
            isBorderDeterminant = 4
            grid[i][j] = 0
            if i>0:
                if grid[i-1][j] in visitedColors:
                    isBorderDeterminant -= 1
                dfs(i-1, j)
            if i<m-1:
                if grid[i+1][j] in visitedColors:
                    isBorderDeterminant -= 1
                dfs(i+1, j)
            if j>0:
                if grid[i][j-1] in visitedColors:
                    isBorderDeterminant -= 1
                dfs(i, j-1)
            if j<n-1:
                if grid[i][j+1] in visitedColors:
                    isBorderDeterminant -= 1
                dfs(i, j+1)
            if isBorderDeterminant>0:
                grid[i][j] = 0
            else:
                grid[i][j] = -1
        
        
        dfs(row, col)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    grid[i][j] = color
                elif grid[i][j] == -1:
                    grid[i][j] = initialColor
        return grid
    
    """
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
    """