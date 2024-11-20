class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        m, n = len(room), len(room[0])
        visited = set() # (i, j, dir) x,y are the directions
        seen = set() # (i, j)
        directions = {'right': (0, 1), 'down': (1, 0), 'left': (0, -1), 'top': (-1, 0)}
        dirs = ['right', 'down', 'left', 'top']

        res = 0

        def dfs(row, col, idx):
            nonlocal res
            #print(row, col, idx)

            if (row, col, idx) in visited:
                return

            visited.add((row, col, idx))
            if (row, col) not in seen:
                res += 1
                seen.add((row, col))
            
            newIdx = idx
            for i in range(4):
                newIdx = (idx + i) % 4
                dr, dc = directions[dirs[newIdx]]
                r, c = row + dr, col + dc
                if (0 <= r < m) and (0 <= c < n) and room[r][c] == 0:
                    dfs(r, c, newIdx)
                    break


        dfs(0, 0, 0)
        return res
