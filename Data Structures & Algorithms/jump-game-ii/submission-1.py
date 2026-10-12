class Solution:
    def jump(self, nums: List[int]) -> int:
        # minimum jump level by level like BFS

        # each jump is counted when moving from current level to all mext index reachable from max reachable jump in the current level


        jump_count = 0
        level_end_idx = 0
        max_reachable_idx = 0

        for i in range(len(nums) - 1):
            # level window is defined based on previous level max reachable jump
            max_reachable_idx = max(max_reachable_idx, i + nums[i])

            if i == level_end_idx:
                jump_count += 1
                # move to next level
                level_end_idx = max_reachable_idx

        return jump_count
        