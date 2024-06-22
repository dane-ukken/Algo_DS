# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        traverse = None
        minHeap = []
        heapq.heapify(minHeap)
        
        for index, l in enumerate(lists):
            if not l:
                continue
            heapq.heappush(minHeap, (l.val, index, l))
        
        if not lists or len(minHeap) == 0:
            return head
        
        _, idx, head = heapq.heappop(minHeap)
        traverse = head
        if head and head.next:
            heapq.heappush(minHeap, (head.next.val, idx, head.next))
        while minHeap:
            val, idx, curr = heapq.heappop(minHeap)
            traverse.next = curr
            traverse = traverse.next
            if curr and curr.next:
                heapq.heappush(minHeap, (curr.next.val, idx, curr.next))
                
            
        return head