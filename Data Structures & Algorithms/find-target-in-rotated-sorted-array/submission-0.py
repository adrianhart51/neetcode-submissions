class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        # if left <= mid, half left is sorted, check if target between left and mid
        # if within left and mid do the binary search there
        # else check the half right

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            # half left sorted
            if nums[left] <= nums[mid]:
                # check target within this left half
                # if yes binary search in this half to find target
                if nums[left] <= target <= nums[mid]:
                    right = mid
                # else search in right half
                else:
                    left = mid + 1
            # half right sorted
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid -1
            
        return -1

