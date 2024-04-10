class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        roomsEnd = []
        
        for start, end in intervals:
            flag = False
            for i in range(len(roomsEnd)):
                if start >= roomsEnd[i]:
                    roomsEnd[i] = end
                    flag = True
                    break
            if not flag:
                roomsEnd.append(end)
        
        return len(roomsEnd)
            