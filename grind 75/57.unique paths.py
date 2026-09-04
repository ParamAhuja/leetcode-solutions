"""
DP memoization
recursion
"""

class Solution:
    def __init__(self):
        self.memo = {(1,1): 1}
    def uniquePaths(self, m: int, n: int) -> int:
        if m==0 or n==0:
            return 0
        if (m, n) in self.memo:
            return self.memo[(m, n)]
        a = self.uniquePaths(m-1, n)
        b = self.uniquePaths(m, n-1)
        self.memo[(m,n)]= a+b
        return a + b