class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # backtrack dfs

        # try all combination including itself

        # if adding new number pass the target, backtrack
        result = []

        # sort nums to make sure can prune when next added element will make total pass target
        nums.sort()

        def dfs(idx: int, combination: List[int], total: int):
            # if total == target add combination to result
            if total == target:
                result.append(combination[:])
                return

            # dfs idx until end of nums
            for j in range(idx, len(nums)):
                 # if total > target backtrack
                if total > target:
                    return

                # add nums idx to combination
                # dfs with added total
                combination.append(nums[j])
                dfs(j, combination, total + nums[j])

                # skip nums idx
                # dfs move idx to next element
                combination.pop()

        dfs(0, [], 0)

        return result
        