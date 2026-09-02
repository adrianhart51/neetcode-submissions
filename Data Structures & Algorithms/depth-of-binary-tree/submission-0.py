# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # use dfs curr depth increment each going one level deeper
        if not root:
            return 0
        # compare left vs right depth, store deeper depth
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        