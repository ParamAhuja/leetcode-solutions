# see 3870
"""
above 10**5 as well
"""
class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        lower_bound = 1000
        while n >= lower_bound:
            ans += (n - lower_bound + 1)
            lower_bound *= 1000
        return ans
