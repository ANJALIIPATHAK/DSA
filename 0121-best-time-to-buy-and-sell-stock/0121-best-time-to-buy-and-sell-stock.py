class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        costPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            sellingPrice = prices[i]
            costPrice = min(costPrice, prices[i-1])
            maxProfit = max(maxProfit, sellingPrice - costPrice)
        return maxProfit


