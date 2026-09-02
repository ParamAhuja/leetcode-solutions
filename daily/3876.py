"""
Construct Uniform Parity Array II

part 1 was just "return True"

math
"""


class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_even = math.inf
        min_odd = math.inf
        for i in nums1:
            if i%2==0:
                min_even = min(min_even, i)
            else:
                min_odd = min(min_odd, i)
        return (min_odd==math.inf or min_even==math.inf or min_odd<min_even)