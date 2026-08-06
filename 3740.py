class Solution:
    # 3740 and 3741: https://leetcode.com/problems/minimum-distance-between-equal-elements/description/
    def minimumDistance(self, nums: List[int]) -> int:
        h={}
        for i, n in enumerate(nums):
            if n in h:
                h[n].append(i)
            else:
                h[n] = [i]


        ans = math.inf
        dist=0
        for n in h:
            l = len(h[n])
            if len(h[n])>=3:
                for i in range(l-2):
                    a = h[n][i]
                    c = h[n][i+2]
                    dist = 2*abs(c-a)
                    ans = min(ans, dist)
        
        return -1 if dist==0 else ans