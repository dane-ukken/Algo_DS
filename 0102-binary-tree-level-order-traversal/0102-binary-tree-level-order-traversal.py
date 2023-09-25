# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        treeNodeList = []
        resultList = []
        rootElementList = [root]
        treeNodeList.append(rootElementList)
        return self.popAndPush(treeNodeList, resultList)
        
    def popAndPush(self, listOfNodes: List[List[TreeNode]], resultList: List[List[int]]):
        recentList = listOfNodes[-1]
        if not recentList:
            listOfNodes.pop()
            return resultList
        
        childList = []
        intList = []
        for node in recentList:
            if node:
                intList.append(node.val)
                if node.left:
                    childList.append(node.left)
                if node.right:
                    childList.append(node.right)
        
        if intList:
            resultList.append(intList)
        listOfNodes.append(childList)
        
        return self.popAndPush(listOfNodes, resultList)