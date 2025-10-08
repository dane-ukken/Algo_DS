class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set((0, 0))
        n = len(grid)
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        minHeap = []
        heapq.heappush(minHeap, (grid[0][0], (0, 0)))
        time = 0

        while minHeap:
            if minHeap[0][0] <= time:
                curr = heapq.heappop(minHeap)
                row, col = curr[1]
                if row == n - 1 and col == n - 1:
                    return time
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (0 <= r < n) and (0 <= c < n) and (r, c) not in visited:
                        visited.add((r, c))
                        heapq.heappush(minHeap, (grid[r][c], (r, c)))
            else:    
                time += 1

        return -1