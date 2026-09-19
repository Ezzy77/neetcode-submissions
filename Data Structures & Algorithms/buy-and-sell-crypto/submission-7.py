class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[l]:
                curr = prices[i] - prices[l]
                profit = max(profit, curr)
            if prices[i] < prices[l]:
                l  = i
        return profit
        