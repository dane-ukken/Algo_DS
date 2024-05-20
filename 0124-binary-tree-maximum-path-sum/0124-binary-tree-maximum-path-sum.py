# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        visited = {}
        def dfs(node):
            if not node:
                return [float(-inf), float(-inf)]
            if node in visited:
                return visited[node]
            val = node.val
            left = dfs(node.left)
            leftTrue = left[0]
            leftFalse = dfs(node.left)[1]
 
            right = dfs(node.right)
            rightTrue = right[0]
            rightFalse = right[1]
            
            maxTrue = max(val, val+rightTrue, val+leftTrue)
            maxFalse = max(rightFalse, leftFalse, leftTrue, rightTrue, val+leftTrue+rightTrue)
            
            visited[node] = [maxTrue, maxFalse]
            return [maxTrue, maxFalse]
            
        res = dfs(root)
        return max(res[0], res[1])