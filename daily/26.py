class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # method 1: convert to set - return list(set(nums))
        # method 2: two pointer - 
        a = 0
        b = 0
        for _ in nums:
            if nums[a]!=nums[b]:
                nums[a+1] = nums[b]
                a+=1
                b+=1
            else:
                b+=1
        return a+1

# arr is nums[:a+1]