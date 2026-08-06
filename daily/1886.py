class Solution:
    # rotate the matrix 90 degree clockwise
    def rotate (self, grid):
        ans = []
        for i in range(len(grid[0])):
            element = []
            for x in grid[::-1]:
                element.append(x[i])
            ans.append(element)
            # print([x[i] for x in grid])
        return ans
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        for _ in range(3):
            mat = self.rotate(mat)
            print(mat)
            if mat == target:
                return True
        return False
