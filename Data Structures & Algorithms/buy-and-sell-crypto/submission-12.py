class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for buy in range(len(prices)):
            for sell in range(buy + 1, len(prices)):
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
        return max_profit
        