class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left, right = 0, 1

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1
        return max_profit



        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         current = prices[j] - prices[i]
        #         max_profit = max(current, max_profit)
        # return max_profit


        