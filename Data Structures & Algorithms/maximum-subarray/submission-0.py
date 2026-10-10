class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sum the subarray window and track the max
        max_sum = nums[0]
        if len(nums) < 2:
            return max_sum

        curr_sum = nums[0]
        # iterate nums keep adding to curr_sum and compare with max
        for i in range(1, len(nums)):
            # if current subarray sum become negative, don't continue the sum
            # because if continue will make the next potential sum lower
            # start counting next subarray instead reset sum to 0 again
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum