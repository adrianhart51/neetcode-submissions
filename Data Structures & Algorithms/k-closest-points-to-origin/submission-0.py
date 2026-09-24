import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use max heap maintain k size
        # inside max heap will be left the closest one
        # because the max heap will pop with farthest one
        max_heap = []
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(max_heap, (dist, x, y))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        res = []
        while max_heap:
            _, x, y = heapq.heappop(max_heap)
            res.append([x, y])
        return res

        