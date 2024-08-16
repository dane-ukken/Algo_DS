class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        visited = set()
        res = 0
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        def dfs(r, c):
            if (r, c) in visited:
                return
            
            visited.add((r, c))
            if grid[r][c] == '0':
                return
            
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if 0<=row<m and 0<=col<n:
                    dfs(row, col)
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    res += 1
                    dfs(i, j)
                
        return res