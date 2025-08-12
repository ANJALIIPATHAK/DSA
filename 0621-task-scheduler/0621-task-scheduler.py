class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskMap = {}
        for task in tasks:
            taskMap[task] = 1 + taskMap.get(task, 0)

        maxHeap = [-cnt for cnt in taskMap.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time