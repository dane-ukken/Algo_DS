# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # Create a dummy node to handle edge cases easily
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move `prev` to the node just before the reversal starts
        for _ in range(left - 1):
            prev = prev.next
        
        # `start` will point to the first node of the segment to be reversed
        start = prev.next
        # `then` will point to the node that will be reversed
        then = start.next
        
        # Reverse the sublist
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next
        
        return dummy.next
