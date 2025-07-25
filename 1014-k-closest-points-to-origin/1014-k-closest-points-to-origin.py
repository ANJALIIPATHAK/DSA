class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceList = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            distanceList.append([distance, x, y])

        heapq.heapify(distanceList)

        res = []
        while(k > 0):
            minDistance, minPointX, minPointY = heapq.heappop(distanceList)
            res.append([minPointX, minPointY])
            k -= 1
        
        return res