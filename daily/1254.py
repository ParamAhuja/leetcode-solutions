# do simple dfs - go to each neigbour, update elements to 2 (visited)
# check if island opens anywhere and return state

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y):
            grid[x][y] = 2
            closed = True
            neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for i, j in neighbours:
                if i<m and i>=0 and j>=0 and j<n:
                    if grid[i][j]==0:
                        closed = (dfs(i, j) and closed)
                else:
                    closed = False
            return closed

        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    continue
                closed = dfs(i,j)
                if closed:
                    ans+=1
        return ans
