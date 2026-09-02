# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invertTreeHelper(root)

    def invertTreeHelper(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case return if node empty
        if not node:
            return
        
        # swap left and right sub tree
        node.left, node.right = node.right, node.left 

        # invert left sub tree
        self.invertTreeHelper(node.left)

        # invert right sub tree
        self.invertTreeHelper(node.right)

        # return
        return node
        