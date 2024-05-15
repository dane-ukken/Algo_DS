# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        first, second = dummy, dummy
        
        while n >= 0:
            first = first.next
            n -= 1
        
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        
        return dummy.next
            
        
        """
        count = 0
        traverse = head
        st = []
        while traverse:
            st.append(traverse)
            traverse = traverse.next
            count += 1
        
        if n == count:
            return head.next
    
        prev = None
        while n >= 0:
            prev = st.pop()
            n -= 1
            
        if prev.next:
            prev.next = prev.next.next
        else:
            prev.next = None
            
        return head
        
        
        """
        """
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
    
        """