# class Solution:
#     def minDays(self, grid: list[list[int]]) -> int:
#         self.n = len(grid)
#         self.m = len(grid[0])
#         return self.helper(grid)
#     def helper(self, grid):
#         ans=0
#         # n = len(grid)
#         # m = len(grid[0])
#         count=self.numIslands(grid)
#         if count==0 or count>=2:
#             return ans
#         elif count==1:
#             for i in range(self.n):
#                 for j in range(self.m):
#                     if grid[i][j] == 1:
#                         ans+=1
#                         grid[i][j]=0
#                         return ans + self.helper(grid)
# # print(grid)
# # print(self.numIslands(grid))
# # print(grid)
# # return 0
#     def numIslands(self, grid):
#         # n= len(grid)
#         # m = len(grid[0])
#         if self.n == 0:
#             return 0
#         cnt = 0
#         for i in range(self.n):
#             for j in range(self.m):
#                 if grid[i][j] == 1:
#                     cnt+=1
#                 self.make_water(i,j,self.n,self.m,grid)
#         return cnt

#     def make_water(self,i,j,n,m,grid):
#         if i<0 or j<0 or i>=n or j>=m:
#             return 0
#         if grid[i][j] == 0:
#             return 0
#         else:
#             grid[i][j]=0
#         self.make_water(i+1,j,n,m,grid)
#         self.make_water(i,j+1,n,m,grid)
#         self.make_water(i-1,j,n,m,grid)
#         self.make_water(i,j-1,n,m,grid)
#         return 0
# grid=[[0,1,1,0],[0,1,1,0],[0,0,0,0]]

# x=Solution()
# print(x.minDays(grid))

class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0])
        # If there are no islands or the grid is already disconnected, return 0.
        if self.numIslands(grid) != 1:
            return 0

        # Try removing each land cell and check if the number of islands increases.
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1:
                    grid[i][j] = 0  # Remove the land cell
                    if self.numIslands(grid) != 1:
                        return 1  # It takes one day to disconnect
                    grid[i][j] = 1  # Restore the land cell

        return 2  # If no single cell disconnection worked, return 2 as the last resort

    def numIslands(self, grid):
        visited = [[False] * self.m for _ in range(self.n)]
        count = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= self.n or j >= self.m or grid[i][j] == 0 or visited[i][j]:
                return
            visited[i][j] = True
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1 and not visited[i][j]:
                    count += 1
                    dfs(i, j)

        return count

# Example usage:
grid = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
x = Solution()
print(x.minDays(grid))  # Output should be 2
