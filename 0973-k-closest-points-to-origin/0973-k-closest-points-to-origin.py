class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [(point[0]*point[0] + point[1]*point[1], point) for point in points]
        heapq.heapify(minHeap)
        closestKPoints = [heapq.heappop(minHeap)[1] for _ in range(k)]
        return closestKPoints