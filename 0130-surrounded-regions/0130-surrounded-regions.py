class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        def dfs_visit(i, j):
            if board[i][j] != 'O':
                return
            board[i][j] = 'U'
            directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
            for dr, dc in directions:
                r, c = i+dr, j+dc
                if r>=0 and r<m and c<n and c>=0:
                    dfs_visit(r, c)
        
        for i in range(m):
            dfs_visit(i, 0)
            dfs_visit(i, n-1)
        
        for j in range(n):
            dfs_visit(0, j)
            dfs_visit(m-1, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'U':
                    board[i][j] = 'O'
        
                