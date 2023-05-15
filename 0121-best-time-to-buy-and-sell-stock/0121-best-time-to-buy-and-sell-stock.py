class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfitVal = 0
        l, r = 0, 1
        
        while(r<len(prices)):
            profit = prices[r] - prices[l]          
            if profit>0 :
                maxProfitVal = max(maxProfitVal, profit)
            else:
                l = r
            r += 1
        
        return maxProfitVal
    
        '''
        n = len(prices)
        maxProfitVal = 0
        maxPrices = [0]*n
        
        for i in range(n):
            if i == 0:
                maxPrices[n-1-i] = prices[n-1-i]
                continue
            maxPrices[n-1-i] = max(maxPrices[n-i], prices[n-1-i])
        
        for i in range(n):
            maxProfitVal = max(maxPrices[i]-prices[i], maxProfitVal)
        
        return maxProfitVal
        '''