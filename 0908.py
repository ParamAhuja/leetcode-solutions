# for j in range(2,-1,-1):
#     print(j)
class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        x=len(grid)-2
        y=len(grid[0])-2

        # no. of 3*3 squares
        # n=x*y
        count=0
        sub=[]
        for i in range(x):
            for j in range(y):
                sub+=[[i,j]]
        print(sub)
        for i in sub:
            magic=True
            sum=0
            for j in range(i[0], i[0]+3):
                sum+=grid[j][i[1]]
            print("sum for grid",i,":",sum)
            elements=[]
            for j in range(i[0], i[0]+3):
                for k in range(i[1],i[1]+3):
                    elements.append(grid[j][k])
                    if grid[j][k]<1 or grid[j][k]>9 or len(elements)!=len(set(elements)):
                        magic=False
                        break
                if magic==False:
                    break
            
            print(elements)

            if magic:
                for j in range(i[0], i[0]+3):
                    s=0
                    for k in range(i[1],i[1]+3):
                        s+=grid[j][k]
                    print(s)
                    if s!=sum:
                        magic=False
                        break
            if magic:
                for j in range(i[1],i[1]+3):
                    s=0
                    for k in range(i[0], i[0]+3):
                        s+=grid[k][j]
                    print(s)
                    if s!=sum:
                        magic=False
                        break
            if magic:
                s=0
                for j in range(0,3):
                    s+=grid[i[0]+j][i[1]+j]
                print(s)
                if s!=sum:
                    magic=False
                    break
            if magic:
                s=0
                for j in range(0,3):
                    s+=grid[i[0]+j][i[1]-j+2]
                print(s)
                if s!=sum:
                    magic=False
                    break
            if magic:
                count+=1

        return count
    
grid=[[9, 4, 6],[ 5, 3, 7], [1, 8, 2]]
# grid=[[2, 9, 4], [7, 5, 3],[ 6, 1, 8]]


x=Solution()
ans=x.numMagicSquaresInside(grid)
print(ans)