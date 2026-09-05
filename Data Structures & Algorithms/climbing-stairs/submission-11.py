class Solution:
    def climbStairs(self, n: int) -> int:
        prevPrev = 1
        prev = 1
        
        for i in range(2, n + 1):
            prevPrev, prev = prev, prev + prevPrev

        return prev

        