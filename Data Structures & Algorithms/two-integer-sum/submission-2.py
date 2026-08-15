class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create map num to index
        num_idx_map = {}
        for idx, num in enumerate(nums):
            if num not in num_idx_map:
                num_idx_map[num] = idx

        # iterate num in nums
        # find remainder = target - num in num_index_map and i != j.
        # if any return current num index and num_index_map[x]
        for idx, num in enumerate(nums):
            remainder = target - num
            if remainder in num_idx_map:
                remainder_idx = num_idx_map[remainder]
                if idx != remainder_idx:
                    return [min(idx, remainder_idx), max(idx, remainder_idx)]

        # You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
        # Only one valid answer exists.

        return []
        