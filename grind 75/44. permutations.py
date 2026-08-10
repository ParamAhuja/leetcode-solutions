"""
O(n!) backtracking algorithm

same as concepts/search/search_permutations.py
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        chosen = [False] * n
        permutations = []
        curr_path = []
        def find_permutations():
            if len(curr_path) == n:
                permutations.append(curr_path[:])
                return
            for i in range(n):
                if chosen[i]:
                    continue
                curr_path.append(nums[i])
                chosen[i] = True

                find_permutations()

                chosen[i] = False
                curr_path.pop()
        find_permutations()
        return permutations