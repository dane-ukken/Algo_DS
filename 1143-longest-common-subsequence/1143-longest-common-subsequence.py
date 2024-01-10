class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for j in range(n)] for i in range(m)]
        poss_dir = ((1, 0), (0, 1))
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1
                    if i+1 < m and j+1 < n:
                        dp[i][j] += dp[i+1][j+1]
                    
                else:
                    for dr, dc in poss_dir:
                        r, c = i+dr, j+dc
                        if c < n and r < m:
                            dp[i][j] = max(dp[i][j], dp[r][c])
        
        return dp[0][0]
        
        
        