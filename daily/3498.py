class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, x in enumerate(s):
            ans += (i+1)*(123 - ord(x))
        return ans