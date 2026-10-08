from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort make sure complete the course that don't have dependency first
        # after completing that course that don't have dependency,
        # if that course is dependency of other course, will reduce dependency of other course when it's completed

        # count indegree of node
        indegree = defaultdict(int)
        adj_list = defaultdict(list)
        for u, v in prerequisites:
            indegree[u] += 1
            adj_list[v].append(u)

        # use bfs process node with 0 indegree
        # indegree 0 means there's no dependency so can process it
        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        result = []
        # when process node, decrement indegree of neighbor node
        while queue:
            node = queue.popleft()
            result.append(node)

        # if neighbor node indegree become 0 add to the queue
        # means all dependency of the neighbor node already resolved so can process
            for nei in adj_list[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        # detect cycle if all node count processed in result not equal with numCourses
        return result if len(result) == numCourses else []
        