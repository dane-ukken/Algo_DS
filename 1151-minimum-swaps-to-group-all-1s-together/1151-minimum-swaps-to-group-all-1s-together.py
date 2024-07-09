class Solution:
    def minSwaps(self, data: List[int]) -> int:
        res = float('inf')
        #find the number of ones
        numCounts = Counter(data)
        windowSize = numCounts[1]
        
        #start a sliding window and measure the min zeroes
        l, r = 0, windowSize-1
        if windowSize == 0:
            return 0
        
        oneCount = Counter(data[:r])[1]
        
        while r < len(data):
            oneCount += data[r]
            res = min(res, windowSize - oneCount)
            oneCount -= data[l]
            
            l += 1
            r += 1
        
        return res
        