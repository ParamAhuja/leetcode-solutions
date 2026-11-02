class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        mid = int(median(nums))
        ans = 0
        for i in nums:
            ans+= abs(i-mid)
        return ans
