class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        # ans = 0
        # n = len(nums)
        # for i in range(n):
        #     if n%(i+1) == 0:
        #         ans+= nums[i]**2
        # return ans
        
        # one liner:
        return sum(list(map(lambda x: x**2, [nums[i] if (len(nums)%(i+1)==0) else 0 for i in range(len(nums))])))