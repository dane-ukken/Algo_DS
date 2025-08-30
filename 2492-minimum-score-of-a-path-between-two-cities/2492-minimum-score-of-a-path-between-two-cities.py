class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        res = float('inf')
        visited = set()
        neighborDict = defaultdict(list)
        q = deque()

        for n1, n2, d in roads:
            neighborDict[n1].append((n2, d))
            neighborDict[n2].append((n1, d))
        
        q.append(1)
        while q:
            l = len(q)
            for i in range(l):
                curr = q.popleft()
                if curr in visited:
                    continue
                visited.add(curr)
                for neighbor, distance in neighborDict[curr]:
                    if neighbor not in visited:
                        q.append(neighbor)
                    res = min(res, distance)
        
        return res