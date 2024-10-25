# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        minHeap = []
        heapq.heapify(minHeap)

        for idx, l in enumerate(lists):
            if not l:
                continue
            heapq.heappush(minHeap, (l.val, idx, l))
        
        traverse = dummy
        while minHeap:
            _, idx, curr = heapq.heappop(minHeap)
            #print(traverse)
            traverse.next = curr
            if curr and curr.next:
                heapq.heappush(minHeap, (curr.next.val, idx, curr.next))
            traverse = traverse.next

        return dummy.next