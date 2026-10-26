# do simple dfs - go to each neigbour, update elements to 0 (visited)
# add all values and return total
# medium

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y):
            total = grid[x][y]%k
            grid[x][y] = 0

            neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for i, j in neighbours:
                if i<m and i>=0 and j>=0 and j<n and grid[i][j]!=0:
                        total += (dfs(i, j)%k)
                        total %= k
            return total

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    continue
                total = dfs(i,j)
                if total%k==0:
                    ans+=1
        return ans
