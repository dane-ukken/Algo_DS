class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        res = []
        result = []
        heapq.heapify(res)
        
        if not newInterval:
            return intervals
        
        if not intervals:
            return [newInterval]
        
        for interval in intervals:
            if start > interval[1] or end < interval [0]:
                heapq.heappush(res, [interval[0], interval])
                continue
            if start >= interval[0]:
                start = interval[0]
            if end <= interval[1]:
                end = interval[1]
        
        heapq.heappush(res, [start, [start, end]])
        
        while len(res):
            result.append(res[0][1])
            heapq.heappop(res)
        
        return result
                
                