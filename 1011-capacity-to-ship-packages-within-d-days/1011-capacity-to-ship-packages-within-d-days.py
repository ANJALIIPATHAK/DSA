class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minCapacity = sum(weights)

        left = max(weights)
        right = sum(weights)

        while left <= right:
            capacity = (left + right) // 2
            totalDays = 1
            currLoad = 0

            for weight in weights:
                if weight + currLoad > capacity:
                    totalDays += 1
                    currLoad = 0
                currLoad += weight

            if totalDays <= days:
                minCapacity = min(minCapacity, capacity)
                right = capacity - 1
            else:
                left = capacity + 1
        return minCapacity

        