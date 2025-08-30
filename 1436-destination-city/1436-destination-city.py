class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        visited = set()
        neighborDict = defaultdict(list)
        for s, d in paths:
            neighborDict[s].append(d)
        
        _, dest = paths[0]
        while True:
            if not neighborDict[dest]:
                break
            dest = neighborDict[dest][0]
        
        return dest