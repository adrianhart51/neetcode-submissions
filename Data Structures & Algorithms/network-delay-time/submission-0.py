from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # start from starting node k visit all nodes
        # from each node visit neighbor nodes with minimum time
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))

        node_time = {}
        # starting node immediately visited
        node_time[k] = 0
        # use priority queue visit node with less time needed first
        pq = [(0, k)]

        while pq:
            time, node = heapq.heappop(pq)

            if time > node_time.get(node, float('inf')):
                continue

            for nei, nei_time in graph[node]:
                new_time = time + nei_time

                if new_time < node_time.get(nei, float('inf')):
                    node_time[nei] = new_time
                    heapq.heappush(pq, (new_time, nei))

        # check if all node visited, if not return -1
        # if all visited return max time when visiting node
        # max time become the minimum required time to visit all nodes
        return max(node_time.values()) if len(node_time) == n else -1

        