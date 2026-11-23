class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        m, n = len(board), len(board[0])

        # find o from edges

        # dfs change reachable o from edges to y
        def dfs(r: int, c: int, board: List[List[str]]):
            if r < 0 or r  >= m or c < 0 or c >= n or board[r][c] != 'O':
                return

            board[r][c] = 'Y'
            for dr, dc in DIRECTIONS:
                dfs(r + dr, c + dc, board)

        for r in range(m):
            dfs(r, 0, board)
            dfs(r, n - 1, board)

        for c in range(n):
            dfs(0, c, board)
            dfs(m - 1, c, board)

        
        # iterate all change o to x, change y to o
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'Y':
                    board[r][c] = 'O'

        # time: O(mn) space: O(mn)
 
        