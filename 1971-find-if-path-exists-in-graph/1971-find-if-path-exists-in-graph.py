class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        edgeDict = defaultdict(list)
        res = False
        
        for start, end in edges:
            edgeDict[start].append(end)
            edgeDict[end].append(start)
            
        def dfs(node):
            nonlocal res
            
            if node in visited:
                return
            
            if node == destination:
                res = True
                
            visited.add(node)
            neighbors = edgeDict[node]
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(source)
        return res