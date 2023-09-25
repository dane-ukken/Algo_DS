# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]        
        if not root:
            return res
        self.countGoodNodes(root, root.val, res)
        return res[0]
        
    
    def countGoodNodes(self, root: TreeNode, greatest: int, count: List[int]) -> int:
        if not root:
            return
        if root.val >= greatest:
            count[0] += 1
        self.countGoodNodes(root.left, max(root.val, greatest), count)
        self.countGoodNodes(root.right, max(root.val, greatest), count)

        