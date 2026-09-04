import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums[:]
        heapq.heapify(self.min_heap)
        # trim down the min heap so will only contain the top K number
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # using min heap will track the "smallest" from top K, so it will become the Kth largest
        heapq.heappush(self.min_heap, val)
        # we don't what's the top 1, 2, 3, but we know the top K because it's the smalles from the top
        # maintain the min heap will only contain K element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # return the smallest of the top k
        return self.min_heap[0]
        
