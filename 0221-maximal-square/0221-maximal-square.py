class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cache = [[-1 for _ in range(n)] for _ in range(m)]
        
        def helper(row, col):
            if row >= m or col >= n:
                return 0 
                
            if cache[row][col] > -1:
                return cache[row][col]

            down = helper(row+1, col)
            right = helper(row, col+1)
            diag = helper(row+1, col+1)
            
            if matrix[row][col] == "0":
                cache[row][col] = 0
                return cache[row][col]

            cache[row][col] = 1 + min(down, right, diag)
            return cache[row][col]
        
        helper(0,0)
        maxLen = max(max(row) for row in cache)
        
        return maxLen ** 2