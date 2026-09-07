from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count each num freq use hashmap

        # hashmap is not sorted
        # opt A iterate hashmap key value convert to list of tuple (value, key), sort the list by the value desc, slice the list 0:k, return the keys -> n log n
        # opt B iterate hashmap key value convert to list of tuple (value, key), push to min heap, pop if heap size > k, return the keys -> n log k

        # implement opt b
        num_freq_dict = defaultdict(int)
        for num in nums:
            num_freq_dict[num] += 1

        num_freq_heap = []
        for key, val in num_freq_dict.items():
            heapq.heappush(num_freq_heap, (val, key))

            if len(num_freq_heap) > k:
                heapq.heappop(num_freq_heap)



        result = []
        for _, num in num_freq_heap:
            result.append(num)

        return result

        