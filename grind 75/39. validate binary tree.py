"""
inorder DFS BST
similar to grind/66
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = -math.inf
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        a = self.isValidBST(root.left)
        if root.val>self.prev:
            self.prev = root.val
        else:
            return False
        b = self.isValidBST(root.right)
        return a and b
