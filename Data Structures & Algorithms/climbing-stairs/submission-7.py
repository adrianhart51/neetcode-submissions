class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {}
        return self.dp(n)
    
    def dp(self, n: int) -> int:
        if n <= 1:
            return 1

        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.dp(n - 1) + self.dp(n - 2)

        return self.memo[n]
        