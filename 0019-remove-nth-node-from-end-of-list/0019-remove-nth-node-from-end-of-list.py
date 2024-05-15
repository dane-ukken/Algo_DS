# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        traverse = head
        while traverse:
            traverse = traverse.next
            count += 1
        
        if n == count:
            return head.next
        
        traverse = head
        prev = None
        newCount = 1
        
        
        while traverse:
            if newCount == count - n + 1:
                temp = traverse.next
                prev.next = temp
                break
            prev = traverse
            traverse = traverse.next
            newCount += 1
        
        return head