class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        freshCount = 0
        m, n = len(grid), len(grid[0])
        activeRots = collections.deque()
        
        def bfs():
            nonlocal time
            nonlocal freshCount
            
            while len(activeRots) > 0:
                if freshCount == 0:
                    return
                
                newRotCount = len(activeRots)
                time += 1
                for i in range(newRotCount):
                    curr = activeRots.popleft()
                    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
                    for dr, dc in directions:
                        x, y = curr[0]+dr, curr[1]+dc
                        if x>=0 and x<m and y>=0 and y<n and grid[x][y] == 1:
                            activeRots.append((x, y))
                            grid[x][y] = 2
                            freshCount -= 1
                    
            time = -1
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshCount += 1
                elif grid[i][j] == 2:
                    activeRots.append((i, j))
        
        if freshCount == 0:
            return time
        bfs()
        return time
        
        
        