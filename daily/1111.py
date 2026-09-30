class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        n = len(seq)
        ans = [0]*n
        stk = []
        maxDepth = 0
        currDepth = 0
        for i in range(n):
            if seq[i] == "(":
                currDepth +=1
                stk.append(i)
                maxDepth = max(maxDepth, currDepth)
                continue
            else:
                if currDepth >= floor(maxDepth//2)+1:
                    ans[stk.pop()] = 1
                    ans[i] = 1
                currDepth -=1
        return ans