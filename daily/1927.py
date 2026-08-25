"""
sum game

math, game theory, greedy
"""

class Solution:
    def sumGame(self, num: str) -> bool:
        Lturns = 0
        Rturns = 0
        Lsum = 0
        Rsum = 0

        n = len(num)
        for i in range(n//2):
            if num[i] == "?":
                Lturns+=1
            else:
                Lsum+=int(num[i])
        for i in range(n//2, n):
            if num[i] == "?":
                Rturns+=1
            else:
                Rsum+=int(num[i])

        # main logic:
        if abs(Lturns-Rturns)%2!=0: # alice always wins
            return True
        else:
            if 2*(Rsum-Lsum) == 9*(Lturns-Rturns): # case for bob to win
                return False
            else:
                return True
