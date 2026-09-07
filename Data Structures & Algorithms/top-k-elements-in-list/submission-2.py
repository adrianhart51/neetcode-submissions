from collections import defaultdict, Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count each num freq use hashmap

        # hashmap is not sorted
        # opt A iterate hashmap key value convert to list of tuple (value, key), sort the list by the value desc, slice the list 0:k, return the keys -> n log n
        # opt B iterate hashmap key value convert to list of tuple (value, key), push to min heap, pop if heap size > k, return the keys -> n log k
        # opt C create bucket of count to num, possible count from 1 -> len(nums), iterate from highest count, add nums in the bucket count, if result reach k then return

        # implement opt C
        n = len(nums)
        bucket = [[] for _ in range(n + 1)]
        
        freq = Counter(nums)
        for num, count in freq.items():
            bucket[count].append(num)

        result = []
        for i in range(n, -1, -1):

            for num in bucket[i]:
                result.append(num)

                if len(result) == k:
                    return result
        

        