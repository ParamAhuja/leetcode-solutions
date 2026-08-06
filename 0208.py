# class Solution:
#     def minSwaps(self, nums: List[int]) -> int:
#         count = float('inf')
#         tot = nums.count(1)
#         for i in range(len(nums)):
#             n=[]
#             for j in range(tot):
#                 n.append(nums[i-j])
#             count_0 = n.count(0)
#             if count > count_0:
#                 count = count_0 
#         return count
class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        tot = nums.count(1)
        l=len(nums)
        count = nums[:tot].count(0)
        nums+=nums[0:tot]
        for i in range(l):
            n=nums[i:i+tot]
            count=min(count,n.count(0))
        return count
    
class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        tot = nums.count(1)
        l = len(nums)
        if tot == 0 or tot == l:
            return 0
        count = nums[:tot].count(0)
        min_count = count
        for i in range(1, l):
            if nums[i - 1] == 0:
                count -= 1
            if nums[(i + tot - 1) % l] == 0:
                count += 1
            min_count = min(min_count, count)
        return min_count