"""sliding window, hashmap
length of longest subarray with at most k frequency
"""

# class Solution:
#     def maxSubarrayLength(self, nums: List[int], k: int) -> int:
#         i = j = 0
#         n = len(nums)

#         hash = {}
#         maxi = 0
#         while(j<n):
#             while nums[j] in hash and hash[nums[j]]==k:
#                 hash[nums[i]]-=1
#                 if hash[nums[i]] == 0:
#                     hash.pop(nums[i])
#                 i+=1
#             if nums[j] in hash:
#                 hash[nums[j]]+=1
#             else:
#                 hash[nums[j]]=1
#             j+=1
#             maxi = max(j-i, maxi)
#         return maxi
        
"""faster: used default dict instead of dict"""
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i = j = 0
        n = len(nums)

        hash = defaultdict(int)
        maxi = 0
        while(j<n):
            while hash[nums[j]]==k:
                hash[nums[i]]-=1
                i+=1
            hash[nums[j]]+=1
            j+=1
            maxi = max(j-i, maxi)
        return maxi
        
