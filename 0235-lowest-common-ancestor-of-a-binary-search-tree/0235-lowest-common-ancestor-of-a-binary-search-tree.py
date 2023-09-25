# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < q.val:
            return self.lowestCommonAncestorSortedInputs(root, p, q)
        return self.lowestCommonAncestorSortedInputs(root, q, p)
    
    def lowestCommonAncestorSortedInputs(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val <= root.val:
            if q.val >= root.val:
                return root
            return self.lowestCommonAncestorSortedInputs(root.left, p, q)
        return self.lowestCommonAncestorSortedInputs(root.right, p, q)