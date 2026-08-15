"""
Longest Subsequence With Non-Zero Bitwise XOR
bit manipulation: xor
# case 1: if xor != 0: return len(nums)
# case 2: if xor == 0 but at least one non zero element exists in num: return len(nums)-1
# case 3: if xor == 0 and all zero elems: return 0
"""

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        nz = 0
        for i in nums:
            nz |= (i>0) # 1 if any non zero exists, 0 o/w
            xor = xor^i # xor of all elements
        return nz * (len(nums) - (not xor)) # covers all cases
