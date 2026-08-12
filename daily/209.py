"""
Minimum Size Subarray Sum
sliding window
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        n = len(nums)
        add = 0
        ans= math.inf
        while(right<n or add>=target):
            if add<target:
                add+=nums[right]
                right+=1
            else:
                ans = min(ans, right-left)
                add-=nums[left]
                left+=1
        if ans!=math.inf:
            return ans
        else:
            return 0