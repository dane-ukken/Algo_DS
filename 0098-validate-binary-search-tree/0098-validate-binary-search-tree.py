# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True
        if not root:
            return True
        return self.isValidSubBST(root, float('-inf'), float('inf'))
            
    
    def isValidSubBST(self, root, minVal, maxVal):
        if not root:
            return True
        if minVal < root.val < maxVal:
            isLeftValid = self.isValidSubBST(root.left, minVal, root.val)
            isRightValid = self.isValidSubBST(root.right, root.val, maxVal)
            return isLeftValid and isRightValid
        else:
            return False
     
        #add min and max in the subTree
        
        """
        if root.left and root.val <= root.left.val:
            res = False
        if root.right and root.val >= root.right.val:
            res = False
        
        isLeftValid = self.isValidBST(root.left)
        isRightValid = self.isValidBST(root.right)      
        
        return res and isLeftValid and isRightValid
        """