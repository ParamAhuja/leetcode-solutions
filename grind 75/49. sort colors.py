"""
method 1: O(2n) - hashmap and update array
method 2: O(3n) - two pointer
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # M1
        # hashMap = Counter(nums)
        # start = 0
        # for i in range(3):
        #     for j in range(start, start+hashMap[i]):
        #         nums[j] = i
        #     start+=hashMap[i]

        
        # M2
        pos = 0
        for i in range(3):
            iterator = 0
            while(iterator<len(nums)):
                if nums[iterator] == i:
                    # swap iter and pos, move pos ahead
                    nums[iterator], nums[pos] = nums[pos], nums[iterator]
                    pos+=1
                iterator+=1