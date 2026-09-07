from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count each num freq use hashmap

        # hashmap is not sorted
        # opt A iterate hashmap key value convert to list of tuple (value, key), sort the list by the value desc, slice the list 0:k, return the keys -> n log n
        # opt B iterate hashmap key value convert to list of tuple (value, key), heapify the list to min heap, pop until heap size <= k, return the keys -> log n

        # implement opt b
        num_freq_dict = defaultdict(int)
        for num in nums:
            num_freq_dict[num] += 1

        num_freq_tuples = []
        for key, val in num_freq_dict.items():
            num_freq_tuples.append((val, key))

        heapq.heapify(num_freq_tuples)

        while len(num_freq_tuples) > k:
            heapq.heappop(num_freq_tuples)

        result = []
        for _, num in num_freq_tuples:
            result.append(num)

        return result

        