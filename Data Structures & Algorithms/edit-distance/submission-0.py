class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # to make word1 equal word2

        m, n = len(word1), len(word2)
        # create dp array
        dp = [[0] * (n + 1) for _ in range (m + 1)]

        print(dp)
        
        # insert char in word1 to make it equal word2
        # base case both word1 and word2 empty -> 0 ops
        # word1 empty but word2 n chars -> n ops
        for i in range(m + 1):
            dp[i][0] = i

        # delete char in word1 to make it equal word2
        # base case both word1 and word2 empty -> 0 ops
        # word1 n chars but word 2 empty -> n ops
        for j in range(n + 1):
            dp[0][j] = j

        # replace char in word1 to make it equal word2
        # base case both word1 and word2 empty -> 0 ops
        # word1 m char and word2 m char with n diff char -> n ops
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # if char at index same between word1 and word2 -> 0 ops
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                 # if chart at index diff between word1 and word2 -> 1 ops + find minimum between insert, delete, replace ops
                    dp[i][j] = 1 + min(
                        dp[i][j - 1],
                        dp[i - 1][j],
                        dp[i - 1][j - 1]
                    )        
       
        return dp[m][n]
        