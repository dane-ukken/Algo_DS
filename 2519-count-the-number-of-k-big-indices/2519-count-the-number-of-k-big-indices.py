class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n <= 2*k:
            return 0

        maxHeapPre, maxHeapPost = [-nums[i] for i in range(k)], [-nums[n-1-i] for i in range(k)]
        heapq.heapify(maxHeapPre)
        heapq.heapify(maxHeapPost)
        
        res = 0
        
        pre, post = [False]*n, [False]*n
        for i in range(k, n-k):            
            if nums[i] <= -maxHeapPre[0]:
                heapq.heappop(maxHeapPre)
                heapq.heappush(maxHeapPre, -nums[i])
            else:
                pre[i] = True
                
            if nums[n-1-i] <= -maxHeapPost[0]:
                heapq.heappop(maxHeapPost)
                heapq.heappush(maxHeapPost, -nums[n-1-i])
            else:
                post[n-1-i] = True

        for i in range(k, n-k):
            if pre[i] and post[i]:
                res += 1
        
        return res