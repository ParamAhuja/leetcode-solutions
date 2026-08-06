class Solution:
    def flatten(self, grid):
        ans = []
        for i in grid:
            ans+=i
        return ans
    def sort(self, arr):
        for i in range(len(arr)-1):
            maxi = i
            for j in range(i+1, len(arr)):
                if arr[j]>arr[maxi]:
                    maxi = j
            arr[maxi], arr[i] = arr[i], arr[maxi]
        return arr

    def mini_abs_diff(self, arr):
        ans = math.inf
        flag = 0
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                continue
            flag = 1
            ans = int( min(fabs(arr[i]-arr[i+1]), ans) )
        if flag == 0:
            return 0
        return ans
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # loop through and get all kxk, sliding window
        # get minimum abs diff - flatten, sort, bubble comparison
        # append to corresponding ans matrix
        ans = []
        
        m = len(grid)
        n = len(grid[0])
        for i in range(m-k+1):
            ans.append([])
            for j in range(n-k+1):
                print("loop starts")
                sub = []
                for c in grid[i:i+k]:
                    sub.append(c[j:j+k])
                print(sub)
                sub = self.flatten(sub)
                print(sub)
                sub = self.sort(sub)
                print(sub)
                ans[i].append(self.mini_abs_diff(sub))
        return ans