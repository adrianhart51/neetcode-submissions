import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use min heap, insert to heap maintain k size
        # if more than k then heappop
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # min_heap now contain k largest nums
        # the next heappop will return kth largest elemtn
        return heapq.heappop(min_heap)
                
            

        
        # use min heap, heapify nums
        # heappop until len(nums) - k
        # when reach len(nums) - k, the heappoped element will be kth largest

        # heapq.heapify(nums)
        # for _ in range(len(nums) - k):
        #     heapq.heappop(nums)

        # return heapq.heappop(nums)
        
        