class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        cycle = set()
        prereqDict = defaultdict(set)
        res = True

        for s, d in prerequisites:
            prereqDict[s].add(d)

        def dfs(node):
            nonlocal res

            if not prereqDict[node]:
                return
            
            if node in cycle:
                res = False
                return 

            if node in visited:
                return
            
            cycle.add(node)
            visited.add(node)
            
            for neighbor in prereqDict[node]:
                dfs(neighbor)

            cycle.remove(node)

            


        for i in range(numCourses):
            visited = set()
            cycle = set()
            dfs(i)
        
        return res