# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        traverse = head
        carry = 0
        
        while(l1 and l2):
            traverse.next = ListNode()
            traverse = traverse.next
            curr = l1.val + l2.val + carry
            traverse.val = curr % 10
            carry = curr // 10
            l1 = l1.next
            l2 = l2.next
        
        while(l1):
            traverse.next = ListNode()
            traverse = traverse.next
            curr = l1.val + carry
            traverse.val = curr % 10
            carry = curr // 10
            l1 = l1.next
            
        while(l2):
            traverse.next = ListNode()
            traverse = traverse.next
            curr = l2.val + carry
            traverse.val = curr % 10
            carry = curr // 10
            l2 = l2.next
        
        if carry:
            traverse.next = ListNode()
            traverse = traverse.next
            traverse.val = 1
            
        return head.next