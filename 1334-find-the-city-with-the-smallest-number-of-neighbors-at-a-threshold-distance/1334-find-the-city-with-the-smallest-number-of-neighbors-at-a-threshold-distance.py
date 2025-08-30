class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        res = 0
        minVal = float('inf')
        neighborDict = defaultdict(list)

        for s, d, w in edges:
            neighborDict[s].append((w, d))
            neighborDict[d].append((w, s))

        def findNeigborCountWithinDistance(node):
            neighborCount = -1
            currDistance = 0
            q = []
            heapq.heappush(q, (0, node))
            visited = set()

            while q:
                l = len(q)
                for i in range(l):
                    d, curr = heapq.heappop(q)
                    if curr in visited or d > distanceThreshold:
                        continue
                    visited.add(curr)
                    neighborCount += 1
                    for distance, neighbor in neighborDict[curr]:
                        if (neighbor not in visited) and (d + distance <= distanceThreshold):
                            heapq.heappush(q, (d+distance, neighbor))

            return neighborCount

        for node in range(n):
            curr = findNeigborCountWithinDistance(node)
            print(node, curr)
            if curr <= minVal:
                res = node
                minVal = curr
        
        return res

#           
#           |
#. 0--------1 (10)
#. |        |
#. 2(1) --- 3(1)
#
#