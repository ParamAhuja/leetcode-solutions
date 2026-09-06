"""
M1: recursion 
M2: dp tabulation bottom up # do again

method:
for each matched character, choose it or not and do recursion base case (t=0 then s=0, same for tabulation)
"""

class Solution:
    def __init__(self):
        self.memo = {}
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) == 0:
            return 1
        if (s,t) in self.memo:
            return self.memo[(s,t)]
        n = len(s)
        ans = 0
        i=0
        while(i<n):
            if s[i] == t[0]:
                ans+= self.numDistinct(s[i+1:], t[1:])
                ans+= self.numDistinct(s[i+1:], t)
                break
            i+=1
        self.memo[(s,t)] = ans
        return ans