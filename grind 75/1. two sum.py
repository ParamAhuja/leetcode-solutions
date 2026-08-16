"""FOR UNSORTED AND SIMPLE SOLUTION: - HASHMAP - check on to go if complementary in hashmap exists
"""        

"""IF ARRAY IS SORTED: 2 POINTER IS BETTER
"""

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         left=0
#         right=len(nums)-1
#         while(left<right):
#             sum = nums[left]+nums[right]
#             if sum == target:
#                 return [left, right]
#             elif sum<target:
#                 left+=1
#             else:
#                 right-=1
        