class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minCPSoFar = [0]*len(prices)
        minCP = prices[0]
        for i in range(0, len(prices)):
            if(prices[i] < minCP):
                minCP = prices[i]
            minCPSoFar[i] = minCP
        
        maxProf = 0
        for i in range(0, len(prices)):
            prof = prices[i] - minCPSoFar[i]
            if(prof > maxProf):
                maxProf = prof

        return maxProf
        

        