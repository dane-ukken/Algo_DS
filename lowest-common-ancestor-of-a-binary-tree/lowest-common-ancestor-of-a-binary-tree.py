# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = root
        
        def dfs(node):
            nonlocal res
            if not node:
                return False
            
            curr = False
            if node == p or node == q:
                curr = True
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            #print(node.val, curr, l, r)
            if (l and r) or (curr and l) or (curr and r):
                res = node

            return l or r or curr
        
        dfs(root)
        return res