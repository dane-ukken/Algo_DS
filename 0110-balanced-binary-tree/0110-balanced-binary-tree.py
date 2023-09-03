# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        result = [True]
        
        def getHeightAndSetResult(root):
            if not root:
                return -1
            
            left = getHeightAndSetResult(root.left)
            right = getHeightAndSetResult(root.right)
            
            if abs(left - right) > 1:
                result[0] = False
            
            return 1 + max(left, right)

        getHeightAndSetResult(root)
        return result[0]
        
        