class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost of idx 0 and 1 is 0
        n = len(cost)
        prev_2 = 0
        prev_1 = 0

        # cost at idx i is min(cost[i - 1], cost[i - 2])
        # because from one idx can move +1 or +2
        for i in range(2, n + 1):
            current = min(
                prev_1 + cost[i - 1],
                prev_2 + cost[i - 2]
            )

            prev_2, prev_1 = prev_1, current
            
        return prev_1
