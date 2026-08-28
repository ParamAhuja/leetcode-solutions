"""
extension of grind/45

interval merge greedy
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        ans = []
        i=0
        # insert all that start before and keep index i where we must insert
        while i<n:
            if intervals[i][0] > newInterval[0]:
                break
            ans.append(intervals[i])
            i+=1

        # now insert at i and merging if needed
        if len(ans)>0 and ans[-1][1] >= newInterval[0]:
            start = min(ans[-1][0], newInterval[0])
            end = max(ans[-1][1], newInterval[1])
            ans.pop()
            ans.append([start, end])
        else:
            ans.append(newInterval)

        # now insert remaining and merging if needed
        while (i<n):
            if ans[-1][1] >= intervals[i][0]:
                start = min(ans[-1][0], intervals[i][0])
                end = max(ans[-1][1], intervals[i][1])
                ans.pop()
                ans.append([start, end])
            else:
                ans = ans + intervals[i:]
                break
            i+=1
        return ans
