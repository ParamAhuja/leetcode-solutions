"""
easy
subarray
"""
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 1
        dec = 1
        ans = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i]>prev:
                dec = 1
                inc += 1
            elif nums[i]<prev:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
            prev = nums[i]
            ans = max(ans, inc, dec)
        return ans


