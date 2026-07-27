class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            dist = abs(x*x + y*y)
            heapq.heappush(minHeap, [dist, x, y])

        res = []
        while(k > 0):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res