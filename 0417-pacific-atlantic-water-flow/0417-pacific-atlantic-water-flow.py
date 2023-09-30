class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []
        
        def dfs_will_flow_to(i, j, target, prevHeight):
            if i<0 or i>=m or j<0 or j>=n or (i, j) in target or prevHeight>heights[i][j]:
                return
            target.add((i, j))
            directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
            for dr, dc in directions:
                r, c = i+dr, j+dc
                dfs_will_flow_to(r, c, target, heights[i][j])
        
        for i in range(m):
            dfs_will_flow_to(i, 0, pac, heights[i][0])
            dfs_will_flow_to(i, n-1, atl, heights[i][n-1])
        
        for j in range(n):
            dfs_will_flow_to(0, j, pac, heights[0][j])
            dfs_will_flow_to(m-1, j, atl, heights[m-1][j])
            
        for i in range(m):
            for j in range(n):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res