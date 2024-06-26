class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = defaultdict(lambda: 0)
        res = []
        for n in nums:
            countDict[n] += 1
            
        max_heap = []    
        for (key, val) in countDict.items():
            max_heap.append((-val, key))
        heapq.heapify(max_heap)
        
        
        while k > 0:
            res.append(heapq.heappop(max_heap)[1])
            k -= 1
        
        return res
        
        '''
        countDict = defaultdict(lambda: 0)
        nBuckets = [[] for i in range(len(nums)+1)]
        res = []
        for n in nums:
            countDict[n] += 1
        for (key, val) in countDict.items():
            nBuckets[val].append(key)
        for i in range(len(nums), 0, -1):
            for v in nBuckets[i]:
                res.append(v)
                if len(res) == k:
                    return res
        return res
        '''