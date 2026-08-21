# todo again
# revise - also see concepts/backtracking

"""
backtracking, searching, combination sum, recursion
"""

class Solution:
    def combos(self, arr, target, sum, curr_path, start):
        if sum == target:
            self.ans.append(curr_path[:])
            return
        if sum>target:
            return
        for i in range(start, len(arr)):
            x = arr[i]
            curr_path.append(x)
            sum+=x
            self.combos(arr, target, sum, curr_path, i)
            curr_path.pop()
            sum-=x

            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 1:
            return []
        self.ans = []
        candidates.sort()
        self.combos(candidates, target, 0, [], 0)
        return self.ans