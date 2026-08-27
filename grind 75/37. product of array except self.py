"""
same as blind/238

math, array

# WITHOUT USING DIVISION in O(2*n)

"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product of array except self
        pre_prod = 1
        suf_prod = 1
        pre = []
        suf = []
        n = len(nums)
        for i in range(len(nums)):
            pre.append(pre_prod)
            pre_prod*=nums[i]

            suf.insert(0, suf_prod)
            suf_prod*= nums[n-i-1]            
        ans = []
        for i in range(len(nums)):
            ans.append(pre[i]*suf[i])
        return ans
