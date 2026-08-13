"""
KADANE's ALGORITHM

method 2: dynamic programming # todo
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum= maxSum = nums[0]

        for i in nums[1:]:
            currentSum = max(i, currentSum+ i)
            maxSum = max(maxSum, currentSum)
            print(currentSum)
        return maxSum


