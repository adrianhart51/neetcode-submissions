class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        for s_char in s:
            s_map[s_char] = s_map.get(s_char, 0) + 1

        t_map = {}
        for t_char in t:
            t_map[t_char] = t_map.get(t_char, 0) + 1

        if len(s_map) != len(t_map):
            return False

        for num in s_map.keys():
            t_num = t_map.get(num, 0)
            if t_num != s_map[num]:
                return False

        return True

        