"""
used to find maximum subarray sum in an array.

at each iteration it checks: 
- either to start a new subarray  if i > currentSum+i - latest element bigger than subarray sum
- or to keep going if currensum+i > i - worth going ahead
note: keep a maxSum var for tracking ans

pseudo code:
currentSum = maxSum = arr[0]

# iterate on rest of elements:

currentSum = max(i, currentSum+i)
maxSum = max(maxSum, currentSum)
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum= maxSum = nums[0]

        for i in nums[1:]:
            currentSum = max(i, currentSum+ i)
            maxSum = max(maxSum, currentSum)
            print(currentSum)
        return maxSum
