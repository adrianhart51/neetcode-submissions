from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check if graph is valid tree 
        # if there's no cycle in the graph
        # all node are connected

        # to check if there's cycle will need to visit all nodes
        # if when visiting node that already visited means it's cycle
        # if cycle return is valid tree false

        # convert the input adjacency list for dfs visit later
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        # Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
        # graph = {
        #     0: [1, 2, 3],
        #     1: [0, 4],
        #     2: [0]
        #     3: [3]
        #     4: [1]
        # }
        # visited: [0, 1]

        # dfs(0, 0)
        # dfs(1, 0)

        # use dfs for visiting node
        print(graph)

# no_cycle
        def no_cycle(node, source):
            visited.add(node)

            neighborhoods = graph[node]
            print(node, neighborhoods)
            
            for nei in neighborhoods:
                print('start-loop', node, source, nei, visited)
                # if node already visited means cycle can directly return false
                if nei in visited:
                    # mark as cycle
                    # print('nei visited', node, source)
                    if nei != source:
                        print('return-false', node, source, nei, visited)
                        return False
                else:
                    print('dfs-nei', node, source, nei, visited)
                    if not no_cycle(nei, node):
                        return False

                print('end-loop', node, source, nei, visited)

            return True

        no_cycle_check = no_cycle(0, 0)
        all_connected = len(visited) == n
        
        return no_cycle_check and all_connected

        # 0: [1, 2, 3]
        