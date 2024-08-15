# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        q = deque()
        if root:
            q.append(root)
        count = 0
        
        while q:
            l = len(q)
            currList = []
            for i in range(l):
                curr = q.popleft()
                currList.append(curr.val)    
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if count % 2 == 1:
                currList.reverse()
            res.append(currList)
            count += 1
                                    
        return res
        
        