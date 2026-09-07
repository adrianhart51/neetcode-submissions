class Solution:

    # challenge if just join the list of str to str using some sort of separator, the separator itself can be a valid char in input list of str
    # need to know how long each str length in input list so can split later in the decode with the exact str length
    def encode(self, strs: List[str]) -> str:
        # [abc, defg, hi, 12, 3456]
        # 3#abc4#defg2#hi2#124#3456

        # str length + # + str
        result = []
        for s in strs:
            result.append(str(len(s)))
            result.append('#')
            result.append(s)

        return ''.join(result)
            

    def decode(self, s: str) -> List[str]:
        # 3#abc4#defg2#hi2#124#3456

        # use pointer to read the length, read current index until found #
        # after # create str read char by char until length then append to result
        result = []

        i = 0
        n = len(s)
        
        while i < n:
            j = i

            # str  3 # a b c 4 # d e f g
            # idx  0 1 2 3 4 5
            # slc 0 1 2 3 4 5

            while s[j] != '#':
                j += 1
            
            # [0:1] -> 3
            length = int(s[i:j])
            i = j + 1
            j = i + length
            # [2:5] -> abc
            string = s[i:j]
            i = j
            
            result.append(string)

        return result


