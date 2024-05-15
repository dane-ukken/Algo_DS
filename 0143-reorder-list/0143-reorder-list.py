# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        prev, traverse = None, None
        
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        if prev:
            prev.next = None
        prev = None
        
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        
        traverse = head
        prev2 = None
        while traverse and prev:
            prev2 = prev
            temp1 = traverse.next
            temp2 = prev.next
            traverse.next = prev
            prev.next = temp1
            traverse = temp1
            prev = temp2
        
        if prev and prev2:
            prev2.next = prev