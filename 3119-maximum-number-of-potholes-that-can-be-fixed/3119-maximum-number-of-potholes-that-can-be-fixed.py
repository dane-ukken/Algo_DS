class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:

        maxHeap = []
        res = 0
        currCount = 0
        for c in road:
            if c == 'x':
                currCount += 1
            elif currCount:
                heapq.heappush(maxHeap, -(currCount + 1))
                currCount = 0
        if currCount:
            heapq.heappush(maxHeap, -(currCount + 1))

        while maxHeap and budget > 0:
            curr = -heapq.heappop(maxHeap)
            if budget > curr:
                budget -= curr
                res += curr - 1
            else:
                res += budget - 1
                budget = 0


        return res