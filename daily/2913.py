"""
Array
Hash Table
Binary Indexed Tree
Segment Tree
"""

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            distinct_values = set()
            for j in range(i, n):
                distinct_values.add(nums[j])
                ans+= len(distinct_values)**2
        return ans
