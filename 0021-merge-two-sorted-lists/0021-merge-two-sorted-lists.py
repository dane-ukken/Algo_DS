# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        '''
        if list1.val < list2.val :
            head = list1
            list1 = list1.next 
        else:
            head = list2
            list2 = list2.next
        '''
        
        traverse = head
        
        while (list1 is not None) and (list2 is not None):
            if list1.val < list2.val :
                traverse.next = list1
                list1 = list1.next 
            else:
                traverse.next = list2
                list2 = list2.next
            traverse = traverse.next
            
        while list1 is not None:
            traverse.next = list1
            list1 = list1.next
            traverse = traverse.next
            
        while list2 is not None:
            traverse.next = list2
            list2 = list2.next
            traverse = traverse.next
            

        return head.next