class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # check greedily if current index is reacheable based on current max reacheable index

        # iterate nums check i reachable and update current max reachable
        max_reachable = 0
        for i in range(len(nums)):
            if i > max_reachable:
                return False
            
            # reachability based on current index and num value of the index
            max_reachable = max(max_reachable, i + nums[i])

        return True
        