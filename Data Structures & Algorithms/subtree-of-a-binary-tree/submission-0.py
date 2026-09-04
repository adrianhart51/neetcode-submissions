# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if empty subRoot -> true
        if not subRoot:
            return True

        # if root empty but subRoot not empty -> false
        if not root and subRoot:
            return False

        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            # if both tree empty -> True
            if not p and not q:
                return True

            # if both not empty and value equal, continue checking it's subtree same also or not
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

            return False

        # find node in root that has same value has subRoot
        if root.val == subRoot.val:
            # if node found, check if node same tree as subRoot
            if isSameTree(root, subRoot):
                return True

        # if node not same tree as subRoot, continue find next matching node and check same tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        # if all node in root don't have same val as subRoot or all node that has matching value not same tree with subRoot -> false
        
        