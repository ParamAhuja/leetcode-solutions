class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
# minimum distance between target and start
        i = 0
        while True:
            right = start+i
            if right<n and nums[right] == target:
                return i
            left = start-i
            if left>=0 and nums[left] == target:
                return i
            i+=1