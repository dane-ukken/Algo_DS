class MedianFinder:

    def __init__(self):
        self.low = [] # maxheap
        self.high = [] # minheap
        heapq.heapify(self.low)
        heapq.heapify(self.high)
        
    def addNum(self, num: int) -> None:
        low, high = self.low, self.high
        
        heapq.heappush(low, -num)

        if low and high and -low[0] > high[0]:
            curr = -1 * heapq.heappop(low)
            heapq.heappush(high, curr)
        
        if len(low) > len(high) + 1:
            curr = -1 * heapq.heappop(low)
            heapq.heappush(high, curr)
        
        if len(high) > len(low) + 1:
            curr = heapq.heappop(high)
            heapq.heappush(low, -curr)
        

    def findMedian(self) -> float:
        low, high = self.low, self.high

        if len(low) > len(high):
            return float(-low[0])
        elif len(low) < len(high):
            return float(high[0])
        else:
            return (high[0]-low[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()