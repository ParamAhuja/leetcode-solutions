"""binary tree - at most 2 child

use stack to traverse bfs

also could have used recursion or bfs using queue # todo

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        stack = [root]
        while (stack):
            node = stack.pop()
            if node.left and node.left!="null":
                stack.append(node.left)
            if node.right and node.right!="null":
                stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root