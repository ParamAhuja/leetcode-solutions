"""
simple dfs 

# instead of visited set, could use a visited matrix or flood fill to change in original matrix
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        ans = 0
        def dfs(coords):
            # print("called dfs for: ", coords)
            # mark all nearby as visited
            x = coords[0]
            y = coords[1]
            # if grid[x][y] == "0":
            #     return
            visited.add((x, y))
            # now call for all neighbours that exist and are "1"
            neighbours = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
            for neighbour in neighbours:
                i = neighbour[0]
                j = neighbour[1]
                if i>=0 and i<m and j>=0 and j<n and grid[i][j]=="1" and ((i,j) not in visited):
                    dfs([i,j])


        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and (i,j) not in visited:
                    dfs([i,j])
                    ans+=1
        return ans