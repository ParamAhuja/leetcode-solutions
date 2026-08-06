""""KADANE'S ALGO - 
""""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        mini = maxi = prices[0]
        for i in prices[1:]:
            mini = min(mini, i)
            profit = max(profit, i-mini)
        return profit

