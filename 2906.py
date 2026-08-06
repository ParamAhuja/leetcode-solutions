class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # product of grid except self
        pre = 1
        ans = []
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            ans.append([])
            for j in range(m):
                ans[-1].append(pre)
                pre*=grid[i][j]%12345
        suf = 1
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                num = (ans[i][j])*(suf)
                suf*= grid[i][j]%12345
                ans[i][j] = (num%12345)
        return ans

        # bad:------------------------------------------
        # pre = 1
        # suf = 1
        # pre_mat = []
        # suf_mat = []
        # n = len(grid)
        # m = len(grid[0])
        # for i in range(n):
        #     pre_mat.append([])
        #     suf_mat.insert(0, [])
        #     for j in range(m):
        #         pre_mat[-1].append(pre%12345)
        #         pre*=grid[i][j]
        #         suf_mat[0].insert(0, suf%12345)
        #         suf*=grid[n-i-1][m-j-1]
        # ans = []
        # for i in range(n):
        #     ans.append([])
        #     for j in range(m):
        #         num = (pre_mat[i][j])*(suf_mat[i][j])
        #         ans[-1].append(num%12345)
        # return ans
