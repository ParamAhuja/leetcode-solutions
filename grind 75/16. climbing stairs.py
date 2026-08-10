""""
Dynamic programming - memoization
Pattern like finbonnaci series
"""

memo = {}
class Solution:
    def climbStairs(self, n: int) -> int:
        if n in memo:
            return memo[n]
        if n == 1 or n==0:
            return 1
        a = self.climbStairs(n-1)
        b = self.climbStairs(n-2)
        memo[n-1] = a
        memo[n-2] = b 
        return a+b