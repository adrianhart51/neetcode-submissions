class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer calculate area between left and right
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            # area = min height(l, r) * (r - l) because water level based on min height(l, r)
            area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, area)

            # try to compare the max by moving l or r that has lower level, because water level bounded by lower level
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_area