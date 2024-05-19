class MedianFinder:

    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        left = bisect.bisect_left(self.stream, num)
        
        self.stream[left: left] = [num]

    def findMedian(self) -> float:

        n = len(self.stream)
        if n % 2 == 0:
            return (self.stream[n//2] + self.stream[n//2 - 1]) / 2
        else:
            return self.stream[n//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()