class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        startTime = customers[0][0]
        totalWaitTime = 0

        for arrivalTime, prepTime in customers:
            if arrivalTime < startTime:
                endTime = startTime + prepTime
            else:
                endTime = arrivalTime + prepTime
            waitTime = endTime - arrivalTime
            totalWaitTime += waitTime
            startTime = endTime
        
        return totalWaitTime / len(customers)