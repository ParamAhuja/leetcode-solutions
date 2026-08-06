
"""graph traversal using stack - dfs type

also could use bfs queue or recursion
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        col = image[sr][sc]

        stack = [[sr, sc]]
        visited = []
        m = len(image)
        n = len(image[0])
        while stack:
            node = stack.pop()
            r = node[0]
            c = node[1]
            print(r, c)
            image[r][c] = color
            visited.append(node)
            # push neighbours if not visited and color is same

            if r+1<=m-1 and [r+1,c] not in visited and image[r+1][c] == col:
                stack.append([r+1,c])
            if r-1>=0 and [r-1,c] not in visited and image[r-1][c] == col:
                stack.append([r-1,c])
            if c+1<=n-1 and [r,c+1] not in visited and image[r][c+1] == col:
                stack.append([r,c+1])
            if c-1>=0 and [r,c-1] not in visited and image[r][c-1] == col:
                stack.append([r,c-1])
        return image

