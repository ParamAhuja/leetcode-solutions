"""
greedy
"""

class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # 1. make sure a solution is possible between mini and maxi
        if 9*num<sum:
            return ""
        # 2. apply greedy for sum-num to maximize score
        q = sum//9
        ans= "9"*(q)
        r = sum%9
        if r>0:
            ans+= str(r)
        return ans+"0"*(num-len(ans))