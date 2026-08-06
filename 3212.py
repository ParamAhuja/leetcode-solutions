class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        ans = 0
        nums_x = []
        nums_y = []

        num_x=0
        num_y=0

        for j in range(len(grid[0])):
            if grid[0][j]=="X":
                num_x+=1
            elif grid[0][j]=="Y":
                num_y+=1
            nums_x.append(num_x)
            nums_y.append(num_y)
            if (num_x==num_y and num_x>=1):
                ans+=1

        for i in range(1, len(grid)):
            num_x=0
            num_y=0
            for j in range(len(grid[0])):
                if grid[i][j]=="X":
                    num_x+=1
                elif grid[i][j]=="Y":
                    num_y+=1
            
                num_x += nums_x[j]
                num_y += nums_y[j]
                if (num_x==num_y and num_x>=1):
                    ans+=1
                num_x-=nums_x[j]
                num_y-=nums_y[j]
                nums_x[j] += num_x
                nums_y[j] += num_y
        return ans