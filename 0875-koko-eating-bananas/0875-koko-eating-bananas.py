class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if n > h:
            return -1
        if n == h:
            return max(piles)
        
        def getBananaHourCount(shortPiles, newH):
            count = 0
            for p in shortPiles:
                count += p//newH
                if p % newH > 0:
                    count += 1
            return count
        
        piles.sort()
        low, high = 1, piles[n-1]
        res = 0
        while low <= high:
            med = low + (high-low)//2
            print(med, low, high)
            bananaHourCount = getBananaHourCount(piles[:], med)
            print(bananaHourCount)
            if bananaHourCount < h:
                high = med - 1
                res = med
            elif bananaHourCount > h:
                low = med + 1
            else:
                res = med
                high = med - 1
        
        return res
                
            
            
            
        
        