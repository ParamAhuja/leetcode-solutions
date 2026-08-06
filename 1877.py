class Solution:
    # def sort(self, arr):
    #     for i in range(len(arr)-1):
    #         maxi = i
    #         for j in range(i+1, len(arr)):
    #             if arr[j]>arr[maxi]:
    #                 maxi = j
    #         arr[maxi], arr[i] = arr[i], arr[maxi]
    #     return arr

    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxi = 0
        for i in range(len(nums)//2):
            maxi = max(maxi, nums[i]+nums[len(nums)-i-1])
        return maxi
