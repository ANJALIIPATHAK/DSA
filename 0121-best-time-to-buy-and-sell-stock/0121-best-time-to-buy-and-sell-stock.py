class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        costPrice = prices[0]
        for i in range(1, len(prices)):
            sellingPrice = prices[i]
            costPrice = min(costPrice, sellingPrice)
            maxProfit = max(maxProfit, sellingPrice - costPrice)
        return maxProfit