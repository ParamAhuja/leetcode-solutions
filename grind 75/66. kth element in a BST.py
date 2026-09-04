"""
inorder DFS
BST
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root==None:
            return
        a = self.kthSmallest(root.left, k)
        if a!=None:
            return a
        # root
        self.count+=1
        if self.count == k:
            return root.val
        b = self.kthSmallest(root.right, k)
        if b!=None:
            return b
