""" Find the Largest Almost Missing Integer
subarrays, array, hashmap

O(2n)
"""

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums)
        hashmap = Counter(nums)
        ans = -1
        if k == 1:
            for i in hashmap:
                if hashmap[i]==1:
                    ans = max(ans, i)
        else:
            if hashmap[nums[0]] == 1:
                ans = nums[0]
            if hashmap[nums[-1]] == 1:
                ans = max(ans, nums[-1])
                  
        return ans

