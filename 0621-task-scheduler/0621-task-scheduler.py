class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        res = 0
        tasksRem = len(tasks)
        taskDict = {}
        for task in tasks:
            if task in taskDict:
                taskDict[task] += 1
            else:
                taskDict[task] = 1
        minHeap = [[-val, key] for key, val in taskDict.items()]
        heapq.heapify(minHeap)
        
        #while heap is not empty
        #   for i in range(n)
        #       eject the tasks in priority queue
        #   add the tasks back with key = key-1
        while tasksRem>0:
            taskListCurr = []
            for i in range(n+1):
                if tasksRem == 0:
                    break
                res += 1
                if len(minHeap) > 0:
                    taskListCurr.append(heapq.heappop(minHeap))
                    tasksRem -= 1
            for taskCount, task in taskListCurr:
                if taskCount <-1:
                    heapq.heappush(minHeap, [taskCount+1, task])
        return res
        
        