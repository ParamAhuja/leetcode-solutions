"""
dp memo
"""

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        memo = {n: 0}
        def climb(step):
            if step in memo:
                return memo[step]

            one = climb(step+1) + ( costs[step] + 1 )

            if step<=n-2:
                two = climb(step+2) + ( costs[step+1] + 4 )
            else:
                two = math.inf
            
            if step<=n-3:
                three = climb(step+3) + ( costs[step+2] + 9 )
            else:
                three = math.inf
            
            cost = min(one, two, three)
            memo[step] = cost
            return cost
        return climb(0)