class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        roomsEnd = []
        heapq.heappush(roomsEnd, intervals[0][1])
        
        for start, end in intervals[1:]:
            if roomsEnd[0] <= start:
                heapq.heappop(roomsEnd)
            heapq.heappush(roomsEnd, end)
        
        return len(roomsEnd)
            