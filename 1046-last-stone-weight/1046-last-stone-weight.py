class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [(-1)*x for x in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            y = (-1)*heapq.heappop(stones)
            x = (-1)*heapq.heappop(stones)  
            #print(x, y)
            if y>x:
                heapq.heappush(stones, x-y)
        if len(stones)>0:
            return (-1)*stones[0]
        return 0