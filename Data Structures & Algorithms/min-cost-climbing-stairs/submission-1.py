class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost of idx 0 and 1 is 0
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0

        # cost at idx i is min(cost[i - 1], cost[i - 2])
        # because from one idx can move +1 or +2
        for i in range(2, n + 1):
            min_cost_idx = (i - 1) if (dp[i - 1] + cost[i - 1]) < (dp[i-2] + cost[i - 2]) else (i - 2)
            dp[i] = dp[min_cost_idx] + cost[min_cost_idx]
            
        return dp[n]
