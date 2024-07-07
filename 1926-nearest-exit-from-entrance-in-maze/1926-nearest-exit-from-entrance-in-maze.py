class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        distance = 0
        m, n = len(maze), len(maze[0])
        q = deque()
        visited = set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        def isExit(x, y):
            if (x == 0 or x == m-1 or y == 0 or y == n-1):
                return True
            
            return False
        
        
        q.append(entrance)
        visited.add((entrance[0], entrance[1]))
        while q:
            distance += 1
            l = len(q)
            
            for i in range(l):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if (row, col) in visited or row < 0 or row == m or col < 0 or col == n or maze[row][col] == '+':
                        continue
                    if isExit(row, col):
                        return distance
                    visited.add((row, col))
                    q.append((row, col))
        
        return -1
                    