class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_seen = float('inf')

        profit = 0
        for price in prices:
            min_seen = min(min_seen, price)
            cur_profit = price - min_seen
            profit = max(profit, cur_profit)

        return profit
        