class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        longest = 0
        char_set = set()
        left = 0

        for right in range(n):
            while s[right] in char_set:
                char_set.discard(s[left])
                left += 1
            longest = max(longest, right - left)
            char_set.add(s[right])

        return longest + 1