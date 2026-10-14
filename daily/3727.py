"""
array, greedy, sorting
"""

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        res = list(map(lambda x: x**2, nums))
        res.sort(reverse = True)
        n = len(res)
        plus = sum(res[:ceil(n/2)])
        minus = sum(res[ceil(n/2):])
        return plus - minus