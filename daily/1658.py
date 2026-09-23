class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        comp = sum(nums) - x
        if comp<0:
            return -1
        if comp == 0:
            return len(nums)
        left = right = 0
        s = 0
        ans = -1
        while(right<len(nums)):
            s+=nums[right]
            while s>comp:
                s-=nums[left]
                left+=1
            if s == comp:
                ans = max(ans, right-left+1)
                print(left, right)
            right+=1
        if ans==-1:
            return -1
        return len(nums) - ans