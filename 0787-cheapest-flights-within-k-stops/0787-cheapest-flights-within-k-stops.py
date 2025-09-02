class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        visited = defaultdict(int)
        neighborDict = defaultdict(list)
        minHeap = []

        for s, d, p in flights:
            neighborDict[s].append((p, d))

        heapq.heappush(minHeap, (0, -1, src))
        while minHeap:
            l = len(minHeap)
            for i in range(l):
                p, stops, node = heapq.heappop(minHeap)
                #print(p, stops, node)
                if visited[node] > 2 * k:
                    continue
                visited[node] += 1
                if node == dst:
                    if stops > k:
                        visited[node] = 0
                        continue
                    else:
                        return p
                for dp, neighbor in neighborDict[node]:
                    newPrice = p + dp
                    heapq.heappush(minHeap, (newPrice, stops + 1, neighbor))
        
        return -1        