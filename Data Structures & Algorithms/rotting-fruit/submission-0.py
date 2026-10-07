from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        # bfs from rotten fruit to make nearby fresh fruit become rotten
        queue = deque([])
        m, n = len(grid), len(grid[0])
        # iterate the cell in the grid, add rotten fruit to queue for starting bfs points
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))

        # for each queue batch, it count as 1 minutes
        minute = 0
        
        while queue:
            batch_size = len(queue)
            rotting_fruit = False
            for _ in range(batch_size):
                curr_r, curr_c = queue.popleft()
                
                for dir_r, dir_c in DIRECTIONS:
                    next_r, next_c = curr_r + dir_r, curr_c + dir_c

                    # boundary validations
                    if next_r < 0 or next_r >= m or next_c < 0 or next_c >= n or grid[next_r][next_c] != 1:
                        continue

                    # make fresh fruit rotten
                    rotting_fruit = True
                    grid[next_r][next_c] = 2
                    queue.append((next_r, next_c))

            if rotting_fruit:
                minute += 1


        # check if there's any fresh fruit left, if yes return -1, else return minutes
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1

        return minute