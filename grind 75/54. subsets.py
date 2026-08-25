"""
method 1. bit masking
take a decimal number (mask) from 0 to 2**(n-1) and loop on its binary rep (length n) hence O(n. 2**n)
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for mask in range(2**n):
            subset = []
            # apply masking and append
            for i in range(n):
                if (mask & (1<<i)):
                    subset.append(nums[i])
            ans.append(subset[:])
        return ans

"""
method 2. Recursion: O(n. 2**n)
"""
# class Solution:
#     def combos(self, nums, path):
#         if len(nums) == 0:
#             self.ans.append(path[:])
#             return
#         x = nums.pop()
#         path.append(x)
#         self.combos(nums, path)
#         path.pop()
#         self.combos(nums, path)
#         nums.append(x)

#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         self.ans = []
#         self.combos(nums, [])
#         return self.ans