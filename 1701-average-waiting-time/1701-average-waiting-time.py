class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        startTime = customers[0][0]
        totalWaitTime = 0

        for arrivalTime, prepTime in customers:
            endTime = max(startTime, arrivalTime) + prepTime
            waitTime = endTime - arrivalTime
            totalWaitTime += waitTime
            startTime = endTime
        
        return totalWaitTime / len(customers)