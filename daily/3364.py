"""
sliding window, prefix sum
"""

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        if n<l:
            return -1
        
        ans = math.inf
        for i in range(n-l+1):
            currSum = sum(nums[i: i+l])
            if currSum>0:
                ans = min(ans, currSum)
            for j in range(i+l, min(n, i+r)):
                currSum += nums[j]
                if currSum>0:
                    ans = min(ans, currSum)
        if ans==math.inf:
            return -1
        return ans        
