class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        seen = set()
        m, n = len(grid), len(grid[0])
        q = deque()
        res = 0
        q.append((0, 0))
        dir = ((0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1))

        while q:
            res += 1
            l = len(q)
            for i in range(l):
                row, col = q.popleft()
                if (row, col) in seen or grid[row][col] == 1:
                    continue
                if row == m - 1 and col == n - 1:
                    return res
                seen.add((row, col))
                for dr, dc in dir:
                    r, c = dr + row, col + dc
                    if 0 <= r < m and 0 <= c < n and (r, c) not in seen:
                        q.append((r, c))

        return -1

        """
       [
        [0,     inf,    inf,    0,      0,      0], 
        [0,     inf,    0,      inf,    inf,    0], 
        [0,     inf,    inf,    0,      inf,    0], 
        [0,     0,      0,      inf,    inf,    0], 
        [inf,   inf,    inf,    inf,    inf,    0], 
        [inf,   inf,    inf,    inf,    inf,    0]
       ]
        """