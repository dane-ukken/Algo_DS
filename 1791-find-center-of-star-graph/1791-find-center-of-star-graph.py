class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        vertices = set()
        
        for i in range(2):
            for j in range(2):
                curr = edges[i][j]
                if curr in vertices:
                    return curr
                vertices.add(curr)
        
        return -1