# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev, traverse = dummy, dummy.next
        
        while traverse and traverse.next:
            one, two = traverse, traverse.next
            traverse = traverse.next.next

            prev.next = two
            two.next = one
            
            
            one.next = traverse
            prev = one
        
        return dummy.next
        
        