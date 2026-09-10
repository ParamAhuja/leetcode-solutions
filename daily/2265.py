# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def rec_avg(self, root):
        if root.left!=None:
            s1, n1 = self.rec_avg(root.left)
        else:
            s1, n1= 0, 0
        
        if root.right!=None:
            s2, n2 = self.rec_avg(root.right)
        else:
            s2, n2= 0, 0
        
        s = root.val + s1 + s2
        n = n1+n2+1
        avg = (s) // (n)
        if root.val == avg:
            self.ans+=1
        return s, n

    def averageOfSubtree(self, root: TreeNode) -> int:
        self.rec_avg(root)
        return self.ans
