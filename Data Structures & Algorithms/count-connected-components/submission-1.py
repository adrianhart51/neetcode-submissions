class DSU:
    def __init__(self, n):
        # node at index i initialize parent as the node itself
        self.parent = list(range(n))
        # initiate current tree size of each node
        self.size = [1] * n

    # find root of the node by checking current parent, after find the root make the root as parent for fast look up, path compresion
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    # union connect node to the existing tree if same parent
    def union(self, u, v):
        # find root of u and v
        ru, rv = self.find(u), self.find(v)
        # if same root return False no union happen
        if ru == rv:
            return False
        # connect root of u and v
        # connect smaller connected node size to larger one
        if self.size[ru] < self.size[rv]:
            ru, rv = rv, ru

        self.parent[rv] = ru
        self.size[ru] += self.size[rv] 

        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # utilize Disjoint Set Union
        # node will point up directly to the parent
        # if node share same parent, connect or merge node to the existing tree with same parent
        # connected nodes will have same root parent

        # init DSU with size n
        dsu = DSU(n)

        component_count = n

        # for each edge union the connected nodes
        for edge in edges:
            if dsu.union(edge[0], edge[1]):
                # reduce component_count every success connect union edge
                component_count -= 1
        
        return component_count


       

    
        