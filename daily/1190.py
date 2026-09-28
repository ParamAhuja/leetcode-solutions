# do again

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        curr = ""
        for i in s:
            if i not in ["(", ")"]:
                curr+=i
                continue
            else:
                if curr!="":
                    stack.append(curr)
                    curr = ""

            if i==")":
                temp = ""
                while (top := stack.pop())!="(":
                    temp+=top[::-1]
                stack.append(temp)
            elif i=="(":
                stack.append(i)
        stack.append(curr)
        return "".join(stack)
                
        # stack = []
        # for i in s:
        #     if i==")":
        #         temp = ""
        #         while (top := stack.pop())!="(":
        #             temp+=top[::-1]
        #         stack.append(temp)
        #     else:
        #         stack.append(i)
        # return "".join(stack)
                