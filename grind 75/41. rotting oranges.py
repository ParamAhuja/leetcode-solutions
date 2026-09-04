"""
graph BFS

similar to the DP problem "min length to nearest zero"
# revise pattern
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        good = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    good+=1
        
        time = 0
        interval = len(q)
        while len(q)!=0:
            if interval==0:
                time+=1
                interval=len(q)
            # try to spread rotten oranges using BFS until flag = 1
            x, y = q.popleft()
            neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for neighbour in neighbours:
                i, j = neighbour
                if i>=0 and i<m and j>=0 and j<n and grid[i][j]==1:
                    # make it rotten
                    grid[i][j] = 2
                    q.append((i,j))
                    good-=1
            interval-=1

        if good==0:
            return time
        return -1

        