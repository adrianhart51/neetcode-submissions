# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs in each level will compare left vs right subtree length
        is_balance = True
        # dfs return current node length, will be used to for parent compare current node length and the other side of the subtree node length
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal is_balance
            # empty tree 0 height
            if not root:
                return 0

            # calc left height
            left = dfs(root.left)
            # calc right height
            right = dfs(root.right)

            # if diff left vs right more than 1 return false
            if abs(left - right) > 1:
                is_balance = False
            
            # return current node height
            return 1 + max(left, right)

        dfs(root)

        return is_balance
        