"""
DP - memoization, dfs
"""
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = {(m-1,n-1): 1}

        def dfs(x, y):
            if (x,y) in memo:
                return memo[(x,y)]

            a=0
            if x+1<m:
                if grid[x+1][y]==0:
                    a = dfs(x+1,y)
                else:
                    i=1
                    j=0
                    direction = "D"
                    while(x+i<m and y+j<n):
                        if grid[x+i][y+j] == 1:
                            if direction=="D":
                                j+=1
                                direction = "R"
                            else:
                                i+=1
                                direction = "D"
                        else:
                            a = dfs(x+i, y+j)
                            break
            b=0
            if y+1<n:
                if grid[x][y+1]==0:
                    b = dfs(x,y+1)
                else:
                    i=0
                    j=1
                    direction = "R"
                    while(x+i<m and y+j<n):
                        if grid[x+i][y+j] == 1:
                            if direction=="D":
                                j+=1
                                direction = "R"
                            else:
                                i+=1
                                direction = "D"
                        else:
                            b = dfs(x+i, y+j)
                            break
            
            memo[(x,y)] = (a+b)%(10**9+7)
            return memo[(x,y)]

        return dfs(0, 0)%(10**9+7)