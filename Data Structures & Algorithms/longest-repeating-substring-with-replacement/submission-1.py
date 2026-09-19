class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # if wildcard k + max freq char within a window < window size
        # then we lack of wildcard to make all char same within the window
        # need to shrink the window
        # track max window length when all wildcard can replace non-max freq char
        # return the max window length

        max_len = 0
        max_freq = 0
        freq = {}
        
        start = 0
        for end in range(len(s)):
            # update current end char freq
            freq[s[end]] = freq.get(s[end], 0) + 1
            max_freq = max(max_freq, freq[s[end]])

            # check wild card can replace all non uniform char in window
            if k + max_freq < end - start + 1:
                # decrease start freq because removed from the window
                freq[s[start]] -= 1
                start += 1

            # update current max window len
            max_len = max(max_len, end - start + 1)

        return max_len

        # k = 1
        # max_len = 5
        # max_freq = 4
        # freq = {a: 2, b: 3}
        # start = 2
        # end = 6
        # AAABABB


            
        