# sorting, binary search

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        # METHOD 0: only works for low constraints: o(n) total
        # lower_count = 0
        # target_count = 0
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         target_count+=1
        #     elif nums[i]<target:
        #         lower_count+=1
        # return list(range(lower_count, lower_count+target_count))

        nums.sort() # others require sorting. o(n.logn)

        # METHOD 1: o(n)
        # return [i for i in range(len(nums)) if nums[i]==target]

        # METHOD 2: o(logn)
        right = len(nums)-1
        left=0
        lb = 0 # first occurance
        while(left<=right):
            mid = left+ (right-left)//2
            if nums[mid] == target:
                lb = mid
            if nums[mid] >= target:
                right = mid-1
            else:
                left = mid+1
        
        right = len(nums)-1
        left = 0
        ub = -1 # last occurance
        while(left<=right):
            mid = left+ (right-left)//2
            if nums[mid] == target:
                ub = mid
            if nums[mid] <= target:
                left = mid+1
            else:
                right = mid-1
        return list(range(lb, ub+1))


