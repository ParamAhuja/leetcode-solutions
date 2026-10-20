"""hard
sorting, subsets
"""

class Solution:
    def peak(self, nums, size):
        """
        return bool
        1. make sure consecutive windows' elements are sorted
        2. make sure within window elements are sorted or mountain peak type /|/
        """
        prevmax = -math.inf
        n = len(nums)
        for i in range(0, n, size):
            window = nums[i: i+size]
            currmax = -math.inf
            currmin = math.inf
            peaked = 0
            prevelem = -math.inf
            for x in (window):
                currmax = max(currmax, x)
                currmin = min(currmin, x)
                if x<prevelem:
                    if peaked==0:
                        peaked=1
                    else:
                        return False
                prevelem = x
            if currmin<prevmax:
                return False
            if peaked ==1 and window[-1]>window[0]:
                return False
            prevmax = currmax
        return True


    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for k in range(1, n+1):
            if n%k!=0: # condn 1
                continue
            if self.peak(nums, k): # condn 2
                ans+=k
                print(k)
        return ans
