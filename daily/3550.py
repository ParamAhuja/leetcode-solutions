class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digi_sum(n):
            s = 0
            while(n!=0):
                s+= (n%10)
                n//=10
            return s
        for i in range(len(nums)):
            if i == digi_sum(nums[i]):
                return i
        return -1