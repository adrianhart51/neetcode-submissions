from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagram if string contain same char and count with another

        # use hashmap char count as key, value list of original str word that has same char count
        result = defaultdict(list)
        for word in strs:
            # input english lower case so can use bucket a-z
            char_count = [0] * 26
            for c in word:
                char_idx = ord(c) - ord('a')
                char_count[char_idx] += 1
            
            key = tuple(char_count)
                
            result[key].append(word)

        return list(result.values())



            
        