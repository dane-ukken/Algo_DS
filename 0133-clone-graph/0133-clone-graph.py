"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeDict = {}
        if not node:
            return
        
        def dfs_copy_node(curr):
            if curr and curr.val in nodeDict:
                return
            
            cloneNode = Node(curr.val)
            nodeDict[curr.val] = cloneNode
            
            for neighbor in curr.neighbors:
                if neighbor.val in nodeDict and nodeDict[neighbor.val] not in cloneNode.neighbors:
                    cloneNode.neighbors.append(nodeDict[neighbor.val])
                    nodeDict[neighbor.val].neighbors.append(cloneNode)
                else:
                    dfs_copy_node(neighbor)
        
        dfs_copy_node(node)
        return nodeDict[node.val]