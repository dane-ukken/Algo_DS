class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[m-1][n-1] = 1
        poss_dir = ((1, 0), (0, 1))
            
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                ways = 0
                for dr, dc in poss_dir:
                    r, c = i+dr, j+dc
                    if r < m and c <n:
                        ways += dp[r][c]
                if i == m-1 and j == n-1:
                    continue
                dp[i][j] = ways
     
        
        return dp[0][0]
        