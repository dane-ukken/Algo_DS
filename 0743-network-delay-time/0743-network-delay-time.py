class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = []
        neighborDict = defaultdict(list)
        visited = set()
        res = 0

        for s, d, w in times:
            neighborDict[s].append((d, w))
        
        heapq.heappush(minHeap, (0, k))
        while minHeap:
            currTime, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            res = max(res, currTime)
            for neighbor, distance in neighborDict[node]:
                newTime = currTime + distance
                heapq.heappush(minHeap, (newTime, neighbor))

        return res if len(visited) == n else -1