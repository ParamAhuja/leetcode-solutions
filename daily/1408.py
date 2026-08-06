# class Solution:
#     def smallestDistancePair(self, nums: List[int], k: int) -> int:
#         n=len(nums)
#         # print(nums)
#         # ans= abs(nums[1]-nums[0])
#         ans=[]
#         ansSet=set()
#         for i in range(n):
#             for j in range(i):
#                 # print((nums[i],nums[j]))
#                 if ((nums[i],nums[j])) not in ansSet:
#                     ansSet.add((nums[i],nums[j]))
#                     # print(ansSet)
#                     # print(nums[i],nums[j])
#                     ans.append(abs( nums[i]-nums[j] ))
#             for j in range(i+1,n):
#                 # print("f", i , j)
#                 # print(nums)
#                 # print((nums[i],nums[j]))
#                 if ((nums[i],nums[j])) not in ansSet:
#                     ansSet.add((nums[i],nums[j]))
#                     # print(ansSet)
#                     # print(nums[i],nums[j])
#                     ans.append(abs( nums[i]-nums[j] ))
#         ans.sort()
#         # print(ans)
#         # print(len(ansSet))
#         # print(ansSet)
#         if len(ans)>k:
#             return ans[k]
#         else:
#             return 0
