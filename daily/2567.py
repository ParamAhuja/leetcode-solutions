class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort() # - can do without it but lazy
        # with even one operation, min abs will get zero always, dont factor that, only see max one
        # take all three possibilities
        
        a = abs(nums[-3] - nums[0])
        b = abs(nums[-2] - nums[1])
        c = abs(nums[2] - nums[-1])

        return min(a, b, c)