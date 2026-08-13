class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        satisfaction = [[customer, grumpy] for customer, grumpy in zip(customers, grumpy)]

        satisfiedCustomers = 0

        for customer, grumpy in satisfaction:
            if grumpy == 0:
                satisfiedCustomers += customer
            else:
                continue
        
        windowSum = 0
        for i in range(0, minutes - 1):
            if satisfaction[i][1] == 1:
                windowSum += satisfaction[i][0]

        maxSatisfiedCustomers = 0
            
        for left in range(0, len(satisfaction) - minutes + 1):
            right = left + minutes - 1
            if satisfaction[right][1] == 1:
                windowSum += satisfaction[right][0]
            maxSatisfiedCustomers = max(maxSatisfiedCustomers, satisfiedCustomers + windowSum)
            if satisfaction[left][1] == 1:
                windowSum -= satisfaction[left][0]
        return maxSatisfiedCustomers
            

