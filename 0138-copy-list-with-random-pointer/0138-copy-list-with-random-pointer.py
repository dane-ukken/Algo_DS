"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeDict = {}
        copyDict = {}
        count = 0
        traverse = head
        copyPreHead = Node(0)
        prev = copyPreHead
        while traverse:
            count += 1
            nodeDict[traverse] = count
            temp = Node(traverse.val)
            prev.next = temp
            prev = temp
            copyDict[count] = temp
            traverse = traverse.next
            
        traverse = head
        copyTraverse = copyPreHead.next
            
        while traverse:
            r = traverse.random
            if not r:
                copyTraverse.random = None
            else:
                idx = nodeDict[r]
                copyRandom = copyDict[idx]
                copyTraverse.random = copyRandom
            traverse = traverse.next
            copyTraverse = copyTraverse.next
        
        return copyPreHead.next
        
        