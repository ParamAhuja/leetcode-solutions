"""
array, math
"""


"""
M1 best:
"""
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(nums) - min(nums)*len(nums)


"""
M2 what i did:
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        a = b = 0
        n = len(nums)
        for i in range(n):
            if nums[a] > nums[i]:
                a = i
            if nums[b] < nums[i]:
                b = i

        ans = nums[b] - nums[a]
        for i in range(n):
            if i == b:
                continue
            ans+= (nums[i] -nums[a])
        return ans
"""