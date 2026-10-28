"""
dynamic programming dp tabulation, bit manipulation xor

my solution:
"""
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for i in range(m)]

        dp[0][0] = set()
        dp[0][0].add(grid[0][0])

        for i in range(1, n):
            dp[0][i] = set()
            for x in dp[0][i-1]:
                dp[0][i].add(x^grid[0][i])
        for i in range(1, m):
            dp[i][0] = set()
            for x in dp[i-1][0]:
                dp[i][0].add(x^grid[i][0])

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = set()
                for x in dp[i-1][j]:
                    dp[i][j].add(x^grid[i][j])
                for x in dp[i][j-1]:
                    dp[i][j].add(x^grid[i][j])
        return min(dp[-1][-1])


"""
editorial: idk # do again
"""
# class Solution:
#     def minCost(self, grid: list[list[int]]) -> int:
#         m, n = len(grid), len(grid[0])

#         dp = [set() for _ in range(n)]
#         dp[0].add(grid[0][0])

#         for i in range(m):
#             for j in range(n):
#                 if i == 0 and j == 0:
#                     continue

#                 value = grid[i][j]
#                 reachable = dp[j] | (dp[j - 1] if j > 0 else set())

#                 dp[j] = {k ^ value for k in reachable}

#         return min(dp[-1])


"""
crazy shit
"""
# class Solution:
#     def minCost(self, g: list[list[int]]) -> int:
#         @cache
#         def f(i,j):
#             if not len(g)>i>=0<=j<len(g[0]): return set()
#             return {g[i][j]^v for v in f(i+1,j)|f(i,j+1)} or {g[i][j]}
        
#         return min(f(0,0))