class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # can only move down or right
        # start 0,0 end m-1,n-1

        # can reach m-1,n-1 from it's top (m-1-1,n-1) and left only (m-1,n-1-1)
        # to reach point x,y, reachable from (x-1, y) and (x, y-1) only
        # number of unique path to reach point(x,y) is number of unique path to reach (x-1, y) + number of unique path to reach (x, y-1)

        memo = {}

        # dfs calculate unique path of point based on it's top and left unique path
        def dfs(r: int, c: int) -> int:
            # if only one row or one column only one path
            if r == 0 or c == 0:
                return 1

            # add memoization so already calculated dfs can directly return from memo instead of calculate again
            memo_key = (r, c)
            if memo_key in memo:
                return memo[memo_key]

            memo[memo_key] = dfs(r - 1, c) + dfs(r, c - 1)

            return memo[memo_key]

        return dfs(m - 1, n - 1)

        