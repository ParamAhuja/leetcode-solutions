"""simple binary search
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) -1
        low = 0

        while low<=high:
            mid = low+(high-low)//2
            if target==nums[mid]:
                return mid
            elif target<nums[mid]:
                high = mid-1
            else:
                low = mid+1
        
        return -1
