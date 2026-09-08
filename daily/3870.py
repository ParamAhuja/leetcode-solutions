"""
# revise
math
"""

class Solution:
    """
    upto 10**5 numbers:
    """
    # def countCommas(self, n: int) -> int:
        # return (n>999)*(n-999)

    """
    above 10**5 as well
    """
    def countCommas(self, n: int) -> int:
        ans = 0
        lower_bound = 1000
        while n >= lower_bound:
            ans += (n - lower_bound + 1)
            lower_bound *= 1000
        return ans

    """
    alt approach
    """
    # def countCommas(self, n: int) -> int:
    #     ans = 0
    #     lower_bound = 999
    #     upper_bound = 999999
    #     x = 1
    #     while n >= lower_bound:
    #         ans += x*(min(n, upper_bound )- lower_bound)
    #         lower_bound = lower_bound*1000 + 999
    #         upper_bound = upper_bound*1000 + 999
    #         x+=1
    #     return ans