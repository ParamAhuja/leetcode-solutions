class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        ans = 0
        sums = []
        sum = 0
        for j in range(len(grid[0])):
            sum += grid[0][j]
            sums.append(sum)
            if sum>k:
                break
            ans+=1
        print(ans)
        for i in range(1, len(grid)):
            sum = 0
            for j in range(len(grid[0])):
                sum+=grid[i][j]
                sums[j]+=sum
                if sums[j]>k:
                    break
                ans+=1
        return ans        