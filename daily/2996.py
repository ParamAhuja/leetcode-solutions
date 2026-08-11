class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        psum = nums[0]
        i = 1
        n = len(nums)
        while(i<n and (nums[i] == nums[i-1] +1)):
            psum+= nums[i]
            i+=1
        print(psum)
        print(i)
        
        x = set(nums)
        for j in range(50):
            if psum in x:
                psum+=1
                continue
            else:
                return psum