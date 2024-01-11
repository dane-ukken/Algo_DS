class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        def dfs(i, isBuying):
            if i >= len(prices):
                return 0
            if (i, isBuying) in dp:
                return dp[(i, isBuying)]
            
            cooldown = dfs(i+1, isBuying)
            if isBuying:
                buy = dfs(i+1, False) - prices[i]
                dp[(i, isBuying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, True) + prices[i]
                dp[(i, isBuying)] = max(sell, cooldown)
            return dp[(i, isBuying)]
        
        return dfs(0, True)
        
        
        
        