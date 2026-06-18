class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        costPrice = prices[0]
        for sellingPrice in prices:
            profit = sellingPrice - costPrice
            maxProfit = max(profit, maxProfit)
            if sellingPrice < costPrice:
                costPrice = sellingPrice
        return maxProfit