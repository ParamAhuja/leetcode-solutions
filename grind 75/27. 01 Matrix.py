"""
# revise
# similar to https://leetcode.com/problems/map-of-highest-peak/description/
bfs, matrix, DP tabulation

method 1: BFS
bfs from zeros and keep updating distance in the same matrix (or we could use a diff matrix and visited set if needed)
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        q = deque([])
        for a in range(m):
            for b in range(n):
                if mat[a][b] == 0:
                    q.append((a,b))
                else:
                    mat[a][b] = "#" # marked as un-processed

        while (len(q)!=0):
            x,y = q.popleft()

            neighbours = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
            for neighbour in neighbours:
                i = neighbour[0]
                j = neighbour[1]
                if i>=0 and i<m and j>=0 and j<n and mat[i][j] =="#":
                    mat[i][j] = mat[x][y]+1
                    q.append((i,j))
                            
        return mat

"""
DP solution:
two passes, top down and bottom up.
take minimum of each

method 1: DP
"""
# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         m, n = len(mat), len(mat[0])

#         for r in range(m):
#             for c in range(n):
#                 if mat[r][c] > 0:
#                     top = mat[r - 1][c] if r > 0 else math.inf
#                     left = mat[r][c - 1] if c > 0 else math.inf
#                     mat[r][c] = min(top, left) + 1

#         for r in range(m - 1, -1, -1):
#             for c in range(n - 1, -1, -1):
#                 if mat[r][c] > 0:
#                     bottom = mat[r + 1][c] if r < m - 1 else math.inf
#                     right = mat[r][c + 1] if c < n - 1 else math.inf
#                     mat[r][c] = min(mat[r][c], bottom + 1, right + 1)

#         return mat