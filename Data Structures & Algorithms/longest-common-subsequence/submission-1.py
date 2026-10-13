class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        
        # text1 and text2 will have each pointer index
        def dfs(i: int, j: int) -> int:        
            # if reach either of text index reach end, return 0
            if i >= len(text1) or j >= len(text2):
                return 0
            
            # add memoization directly return if already calculated previously
            key = (i, j)
            if key in memo:
                return memo[key]
            
            # if char same at both index, increment the result, move both idx at the same time
            if text1[i] == text2[j]:
                memo[key] = 1 + dfs(i + 1, j + 1)
                return memo[key]

            # if char idx different try to check result move the text1 idx and check result move text2 idx, return the max between those 2 result
            memo[key] = max(dfs(i + 1, j), dfs(i, j + 1))
            return memo[key]

        return dfs(0, 0)