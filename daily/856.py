class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in s:
            if i=="(":
                stack.append("(")
            else:
                score = 0
                while (stack[-1]!="("):
                    score += stack.pop()
                stack.pop()
                stack.append( max(1, 2*score) )
        return sum(stack)
                