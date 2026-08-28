"""
greedy merge intervals

check grind/26 for extension of problem
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start time
        # check if end of one > start of next. then merge it, and append it to ans
        # otherwise append directly to ans 
        # edgecase: if multiple are overlapping

        intervals.sort()

        ans = [intervals[0]]

        for j in range(1, len(intervals)):
            if ans[-1][1] >= intervals[j][0]:
                start = min(ans[-1][0], intervals[j][0])
                end = max(ans[-1][1], intervals[j][1])
                ans.pop()
                ans.append([start, end])
            else:
                ans.append(intervals[j])
        return ans