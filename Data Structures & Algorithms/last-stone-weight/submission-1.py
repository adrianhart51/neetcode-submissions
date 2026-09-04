import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # to get two biggest stone will use max heap
        # python heap is min heap, use negative num to "make it max heap"
        if len(stones) == 0:
            return 0

        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        # keep doing until len(max heap) <= 1
        while len(max_heap) > 1:
            # heappop two stone, multiple negative to revert to original val
            stone_1 = -heapq.heappop(max_heap)
            stone_2 = -heapq.heappop(max_heap)

            remaining_stone = abs(stone_1 - stone_2)

            # abs(s1 - s2), if > 0 put back to max heap
            if remaining_stone > 0:
                heapq.heappush(max_heap, -remaining_stone)

        # multiple negative revert back original val
        return -max_heap[0] if len(max_heap) else 0