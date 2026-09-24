# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        q = deque()
        q.append(root)
        result = []

        while q:
            level_size = len(q)
            level_nodes = []
            
            for _ in range(level_size):
                node = q.popleft()
                if node:
                    level_nodes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level_nodes:
                result.append(level_nodes)
        
        return result
