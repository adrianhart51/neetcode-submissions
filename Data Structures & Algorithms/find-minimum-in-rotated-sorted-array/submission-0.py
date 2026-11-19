class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        # if mid > right, left = mid + 1
        # if mid <= left, right = mid

        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
        