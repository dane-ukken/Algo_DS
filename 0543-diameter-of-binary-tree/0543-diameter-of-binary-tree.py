# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = [0]
        
        def getHeightAndSetDiameter(root):
            if not root:
                return -1
            
            leftHeight = getHeightAndSetDiameter(root.left)            
            rightHeight = getHeightAndSetDiameter(root.right)

            maxDiameter[0] = max(maxDiameter[0], 2 + leftHeight + rightHeight)
            
            return 1 + max(leftHeight, rightHeight)
            
        
        getHeightAndSetDiameter(root)
        return maxDiameter[0]
            
        
        
        '''
        if not root:
            return 0
        
        leftTreeDepth = self.maxDepth(root.left)
        rightTreeDepth = self.maxDepth(root.right)
        diameter = leftTreeDepth + rightTreeDepth
        
        return max(diameter, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    '''