class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqMap = dict()
        for i in range(numCourses):
            preReqMap[i] = []
        for c, p in prerequisites:
            preReqMap[c].append(p)
        visitSet = set()
        def dfs(course):
            if course in visitSet:
                return False
            if preReqMap[course] == []:
                return True
            visitSet.add(course)
            for preReq in preReqMap[course]:
                if not dfs(preReq):
                    return False
                preReqMap[course].remove(preReq)
            visitSet.remove(course)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
            