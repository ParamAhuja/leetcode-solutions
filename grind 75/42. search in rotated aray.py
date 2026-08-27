"""
# revise

nice problem of binary search
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while(high>=low):
            middle = (low+high)//2
            if nums[middle] == target:
                return middle
            if nums[low]<=nums[middle]:
                # first half is sorted
                if target<nums[middle] and target>=nums[low]:
                    high = middle-1
                else:
                    low = middle+1
            else:
                # second half is sorted
                if target>nums[middle] and target<=nums[high]:
                    low = middle+1
                else:
                    high = middle-1
        return -1
