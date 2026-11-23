class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []
        # backtrack put closing and opening count close and open count
        def dfs(openN, closeN):
            if openN == closeN == n:
                result.append("".join(stack))
        # if open < n add open
            if openN < n:
                stack.append('(')
                dfs(openN + 1, closeN)
                stack.pop()
        # if close < open add close
            if closeN <  openN:
                stack.append(')')
                dfs(openN, closeN + 1)
                stack.pop()

        # if open == close == n append to result


        dfs(0, 0)

        return result