class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqMap = dict()
        output = []
        for i in range(numCourses):
            prereqMap[i] = []
        for crs, pre in prerequisites:
            prereqMap[crs].append(pre)
        visited, cycle = set(), set()
        
        def dfs(course):
            if course in visited:
                return True
            if course in cycle:
                return False
            cycle.add(course)
            for pre in prereqMap[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return output