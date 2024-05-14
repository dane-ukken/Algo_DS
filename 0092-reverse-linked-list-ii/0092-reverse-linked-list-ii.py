# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        prev = None
        res = head
        lNext, rNext = head, None
        temp = None
        
        if left == right:
            return head
        
        while head and count <= right:
            if count == left:
                lNext = prev
                l = head
            if count == right:
                rNext = head
                
            temp = head.next
            if count <= right and count >= left:
                head.next = prev
            prev = head
            head = temp
            count += 1
        

        if lNext:
            temp = lNext.next
            lNext.next = prev
            temp.next = head
        else:
            res = rNext
            l.next = head
        
        
        
        return res
        