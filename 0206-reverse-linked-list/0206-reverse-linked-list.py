# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        travel = head
        temp = ListNode()
        prev = None

        while(travel is not None):
            temp = travel.next
            travel.next = prev
            prev = travel
            travel = temp
        
        return prev
                