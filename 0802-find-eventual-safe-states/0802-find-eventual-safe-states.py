class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited, unsafeNodes = set(), set()
        edgeDict = defaultdict(lambda: [])
        cycle = set()
        
        def dfs(node):
            if node in cycle or node in unsafeNodes:
                unsafeNodes.update(cycle)
                return
            if node in visited:
                return
            cycle.add(node)
            print('O')
            for des in graph[node]:
                dfs(des)
            
            cycle.remove(node)
            visited.add(node)
            
        for i in range(len(graph)):
            dfs(i)

        res = visited.difference(unsafeNodes)
        res = list(res)
        res.sort()
        return res