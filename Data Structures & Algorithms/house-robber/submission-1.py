class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob i and i+2 or skip i and rob i+1
        # at i+2 max rob result is max(i and i+2, i+1)
        # at i = max(i-2 and i, i-1)

        n = len(nums)

        # create dp array
        dp = [0] * n
        # base case 
        # - no house rob result 0
        if n == 0:
            return 0
        # - 1 house rob result the only house
        if n == 1:
            return nums[0]
            
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            # rob i and i+2 or skip i and rob i+1
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]

        
        
        