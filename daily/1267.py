class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        ans = 0

        for i in range(m):
            ser = 0
            temp = set()
            for j in range(n):
                if grid[i][j] == 1:
                    ser+=1
                    temp.add((i,j))
            if ser>1:
                ans+=ser
                visited.update(temp)
        
        for j in range(n):
            vis = 0
            ser = 0
            for i in range(m):
                if grid[i][j] == 1:
                    ser+=1
                    if (i,j) in visited:
                        vis+=1
            if ser>1:
                ans+= (ser - vis)
        return ans