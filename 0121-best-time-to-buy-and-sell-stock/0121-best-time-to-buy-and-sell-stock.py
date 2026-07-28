class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        costPrice = prices[0]
        for i in range(0, len(prices)):
            sellingPrice = prices[i]
            costPrice = min(sellingPrice, costPrice)
            maxProfit = max(maxProfit, sellingPrice - costPrice)
        return maxProfit