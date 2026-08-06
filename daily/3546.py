class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # Equal Sum Grid partition I
        row_prefix_sum = [0]*len(grid)
        col_sum = [0]*len(grid[0])
        total_sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total_sum+=grid[i][j]
                col_sum[j]+=grid[i][j]
            row_prefix_sum[i]+=total_sum
        for i in row_prefix_sum:
            if i == total_sum-i:
                return True
            if i > total_sum-i:
                break
        cumulative = 0
        for i in col_sum:
            cumulative+=i
            if cumulative == total_sum-cumulative:
                return True
            if cumulative > total_sum-cumulative:
                break
            
        return False