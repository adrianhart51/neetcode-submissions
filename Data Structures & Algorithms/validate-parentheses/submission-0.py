class Solution:
    def isValid(self, s: str) -> bool:
        CHAR_MAP = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        
        stack = []
        for c in s:
            if c in CHAR_MAP:
                if len(stack) == 0:
                    return False
                if stack[-1] != CHAR_MAP[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0

        