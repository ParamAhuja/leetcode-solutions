class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        ans = 0
        for i in s:
            if i=="(":
                stack.append("(")
            else:
                if len(stack)>0:
                    stack.pop()
                else:
                    ans+=1
        ans+=len(stack)
        return ans
