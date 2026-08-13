# revise
"""ALTERNATE SOLUTION:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

"""
"""
binary tree dfs
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root):
        if not root.left and not root.right:
            return 0
        if root.right:
            a = self.depth(root.right)
        else:
            a = 0
        if root.left:
            b = self.depth(root.left)
        else:
            b = 0
        return 1+ max(a,b)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = self.depth(root)
        return 1+ans