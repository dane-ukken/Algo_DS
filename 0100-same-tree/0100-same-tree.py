# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q and p.val != q.val:
            return False
        
        if not p:
            if q:
                return False
            return True
        
        if not q and p:
            return False
        
        leftTruthValue = self.isSameTree(p.left, q.left)
        rightTruthValue = self.isSameTree(p.right, q.right)
        
        return leftTruthValue and rightTruthValue