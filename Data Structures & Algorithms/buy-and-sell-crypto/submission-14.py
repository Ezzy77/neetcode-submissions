class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        b = 0
        s = 1

        while s < len(prices):
            if prices[b] < prices[s]:
                profit = prices[s] - prices[b]
                max_profit = max(max_profit, profit )
            else:
                b = s
            s += 1
        return max_profit
        