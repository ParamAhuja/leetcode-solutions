class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)-1):
            # distance between points[i] and points[i+1]
            ans += max(fabs(points[i][0]-points[i+1][0]), fabs(points[i][1]-points[i+1][1]))
        return int(ans)