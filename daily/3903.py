"""Smallest Stable Index II and I are same (I can also take brute force - low constraints)
prefix sum
Prefix Max and Suffix Min

"""

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        post = []
        pre = []
        maxi = -math.inf
        mini = math.inf
        for i in range(n):
            maxi = max(maxi, nums[i])
            pre.append(maxi)
            mini = min(mini, nums[n-i-1])
            post.append(mini)
        for i in range(n):
            diff = pre[i] - post[n-i-1]
            if diff<=k:
                return i
        return -1

        