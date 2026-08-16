# revise
"""diameter of binary tree

recursive dfs and check diameter at each 
keep track of global var maxLen at each node
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxLen = 0
    def dfs(self, root):
        if root.left:
            max_l = 1+self.dfs(root.left)
        else:
            max_l = 0
        
        if root.right:
            max_r = 1+self.dfs(root.right)
        else:
            max_r = 0
        
        maxThrough = max_l+ max_r
        self.maxLen = max(self.maxLen, maxThrough)

        return max(max_l, max_r)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.maxLen

