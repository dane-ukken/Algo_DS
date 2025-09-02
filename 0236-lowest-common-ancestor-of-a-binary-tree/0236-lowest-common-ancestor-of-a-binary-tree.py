# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = root

        def dfs(head):
            nonlocal res
            if not head:
                return False
            
            mid = head == p or head == q
            
            left = dfs(head.left)
            right = dfs(head.right)

            if (left and right) or (left and mid) or (mid and right):
                res = head
            
            return left or right or mid
        

        dfs(root)
        return res
