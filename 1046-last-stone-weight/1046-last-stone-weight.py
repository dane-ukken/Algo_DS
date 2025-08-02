class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = 0
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            first, second = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            if first > second:
                heapq.heappush(maxHeap, -(first - second))

        return -maxHeap[0] if maxHeap else 0