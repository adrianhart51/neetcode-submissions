class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_idx = {}

        # iterate idx, num in nums
        for idx, num in enumerate(nums):
            # calculate remainder = target - num
            # if remainder in remainder_seen return remainder seen idx, curr idx
            remainder = target - num
            if remainder in seen_idx:
                remainder_idx = seen_idx[remainder]
                return [remainder_idx, idx]
            # If complement is not seen, store current number and its index
            seen_idx[num] = idx

        # You may assume that every input has exactly one pair of indices i and j that satisfy the condition
        # Only one valid answer exists.
        
        return []
        
        

        