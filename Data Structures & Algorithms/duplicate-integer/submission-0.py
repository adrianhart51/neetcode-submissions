class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set(nums)
        return len(nums) > len(unique_nums)
        