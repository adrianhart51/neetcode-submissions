import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use min heap, heapify nums
        # heappop until len(nums) - k
        # when reach len(nums) - k, the heappoped element will be kth largest

        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)
        
        