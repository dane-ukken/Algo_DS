class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])        
        
        res, count = 0, 0
        s, e = 0, 0
        
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                count += 1
                res = max(count, res)
            else:
                e += 1
                count -= 1
        
        return res