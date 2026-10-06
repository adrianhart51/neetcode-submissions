class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs will mark connected land as water after visited
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        m, n = len(grid), len(grid[0])

        def dfs(r: int, c: int, grid: List[List[str]]):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            for dr, dc in DIRECTIONS:
                dfs(r + dr, c + dc, grid)
        
        # iterate cells, when found land increase island count and do dfs
        island_count = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    island_count += 1
                    dfs(r, c, grid)

        return island_count
        
        