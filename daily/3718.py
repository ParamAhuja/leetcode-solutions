"""
easy hashmap
"""

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        hashmap = Counter(nums)
        factor = 1
        while(factor<=101):
            multiple = factor*k
            if (multiple) not in hashmap:
                return multiple
            factor+=1
