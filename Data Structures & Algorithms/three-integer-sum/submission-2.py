class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # utilize two pointer

        # len validation early return
        if len(nums) < 3:
            return []

        # sort the nums
        nums.sort()

        result = []

        # i + j + k, = 0 add to result, < move left, > move right
        i = 0
        while i < len(nums):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    # if pair match add to result
                    result.append([nums[i], nums[left], nums[right]])
                    # prevent duplicate move index until the next index element not same
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1

                    left += 1
                    right -= 1
            
            # skip duplicate i
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            i += 1

        return result

        
        