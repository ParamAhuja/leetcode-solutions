class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        depth = 0
        for i in s:
            if i=="(":
                if depth != 0:
                    ans+=i
                depth+=1
            elif i==")":
                depth-=1
                if depth != 0:
                    ans+=i
        return ans