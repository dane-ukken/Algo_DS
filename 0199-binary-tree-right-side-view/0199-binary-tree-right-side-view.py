# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        resultList = []
        
        if not root:
            return resultList
        
        q = collections.deque()
        q.append(root)

        while q:
            levelLength = len(q)
            for i in range(levelLength):
                node = q.popleft()
                rightSideNode = None
                if node:
                    rightSideNode = node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            resultList.append(rightSideNode.val)
        
        return resultList
                
                