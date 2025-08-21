class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        seen = set()
        m, n = len(grid), len(grid[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        res = 0

        def dfs(r, c):
            if (r, c) in seen:
                return 0
            seen.add((r, c))
            neighborSum = 0
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if 0 <= row < m and 0 <= col < n and grid[row][col] > 0:
                    neighborSum += dfs(row, col)
        
            return grid[r][c] + neighborSum

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and (i, j) not in seen:
                    islandVal = dfs(i, j)
                    if islandVal % k == 0:
                        res += 1

        return res
