# class Solution:
#     def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
#         arr=[]
#         for i in range(0,n):
#             for j in range (i,n):
#                 sub_arr_sum=0
#                 for k in  range(i,j+1):
#                     sub_arr_sum+=nums[k]
#                     #subarray
#                 arr.append(sub_arr_sum)
#                 #subarrays
#             pass
#         arr.sort()
#         print(arr)
#         return sum(arr[left-1:right])

class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        arr=[]
        for i in range(n):
            for j in range (i,n):
                arr.append(sum(nums[i:j+1]))
        arr.sort()
        return sum(arr[left-1:right]) % (10**9 + 7)