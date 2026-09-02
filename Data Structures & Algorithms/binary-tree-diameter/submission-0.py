# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # track current max
        curr_max = 0

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal curr_max
            # diameter = max(length sub left) + max(length sub right)

            
            # in each sub tree calculate diameter and update current max if bigger
            
            # empty tree 0 diameter
            if not root:
                return 0

            # calc height left
            left = dfs(root.left)

            # calc height right
            right = dfs(root.right)

            # calc max diameter
            curr_max = max(curr_max, (left + right))

            # return current node height
            return 1 + max(left, right)

        dfs(root)

        return curr_max



        