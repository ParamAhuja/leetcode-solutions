# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanced(self, root):
        if not root.right and not root.left:
            return 0
        
        if root.right:
            a = 1+self.balanced(root.right)
        else:
            a = 0
        if root.left:
            b = 1+self.balanced(root.left)
        else:
            b = 0
        # print("a is: ", a)
        # print("b is: ", b)
        # print()
        if a==-1 or b==-1:
            return -1

        if fabs(a-b)>1:
            return -1
        return max(a, b)
        # if 
        # return 1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        a = self.balanced(root)
        # print(a)
        if a!=-1:
            return True
        return False
