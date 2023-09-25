# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < q.val:
            if p.val <= root.val:
                if q.val >= root.val:
                    return root
                return self.lowestCommonAncestor(root.left, p, q)
            return self.lowestCommonAncestor(root.right, p, q)
        
        return self.lowestCommonAncestor(root, q, p)
            