# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        delSet = set(to_delete)
        
        def traverseAndDel(r, p, direction, delSet):
            if len(delSet) == 0 or not r:
                return
            
            if r.val not in delSet:
                traverseAndDel(r.left, r, 0, delSet)
                traverseAndDel(r.right, r, 1, delSet)
                return
        
            delSet.remove(r.val)
            if r in res:
                res.remove(r)
            if p:
                if direction == 0:
                    p.left = None
                else:
                    p.right = None
            
            if r.left:
                res.append(r.left)
                
            if r.right:
                res.append(r.right)
            
            traverseAndDel(r.left, None, 0, delSet)
            traverseAndDel(r.right, r, None, delSet)
        
        res.append(root)
        traverseAndDel(root, None, -1, delSet)
        return res