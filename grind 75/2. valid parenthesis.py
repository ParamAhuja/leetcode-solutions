""" use stack
expression resolution
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(": ")", "{": "}", "[": "]"}
        for i in s:
            if i in ["(", "{", "["]:
                stack.append(i)
            elif len(stack)>0 and i == pairs[stack[-1]]:
                stack.pop()

            else:
                return False
        if len(stack)==0:
            return True
        return False