class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        
        intervals.sort()
        prev = intervals[0]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prev[1]:
                return False
            prev = intervals[i]

        return True