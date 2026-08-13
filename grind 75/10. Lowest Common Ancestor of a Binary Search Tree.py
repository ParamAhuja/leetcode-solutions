# revise
""" USE PROPERTY OF binary search tree THAT LEFT IS LOWER AND RIGHT IS LARGER, 
solve using recursion

given p!=q

binary search tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if min(p.val, q.val)<=root.val and max(p.val, q.val) >= root.val:
            return root
        elif p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
