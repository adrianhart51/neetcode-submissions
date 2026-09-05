class Solution:
    def climbStairs(self, n: int) -> int:
        current = 0
        prevPrev = 1
        prev = 1
        
        for i in range(2, n + 1):
            current = prev + prevPrev
            prevPrev = prev
            prev = current

        return prev

        