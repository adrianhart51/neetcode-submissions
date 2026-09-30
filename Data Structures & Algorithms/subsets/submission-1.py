class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # dfs backtrack
        result = []
        def dfs(idx: int, path: List[int]):
            # basecase when index processed until the end of input, append the subset to result
            if idx >= len(nums):
                result.append(path[:])
                return

            # include current index to subset
            path.append(nums[idx])
            dfs(idx + 1, path)

            # exclude current index from subset
            path.pop()
            dfs(idx + 1, path)

        dfs(0, [])
        return result
        