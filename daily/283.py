# Move Zeroes to end of array
#  my two pointer solution - 
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 flag = 0
#                 for j in range (i+1, len(nums)):
#                     if nums[j]!=0:
#                         flag=1
#                         nums[i], nums[j] = nums[j], nums[i]
#                         break
#                 if flag == 0:
#                     break

# clever solution -
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1