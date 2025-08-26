# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkBST(node, minLimit, maxLimit):
            if not node:
                return True
            
            if not minLimit < node.val < maxLimit:
                return False
            
            return checkBST(node.left, minLimit, min(node.val, maxLimit)) and checkBST(node.right, max(node.val, minLimit), maxLimit)

        
        return checkBST(root, float('-inf'), float('inf'))