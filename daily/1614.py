class Solution:
    def maxDepth(self, s: str) -> int:
        currDepth = 0
        ans = 0
        for i in s:
            if i=="(":
                currDepth+=1
            elif i==")":
                currDepth-=1
            ans = max(ans, currDepth)
        return ans
