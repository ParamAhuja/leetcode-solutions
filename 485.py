class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        count = 0
        for i in nums:
            if i==1:
                count+=1
            else:
                maxi = max(maxi, count)
                count = 0
        maxi = max(maxi, count)
        return maxi