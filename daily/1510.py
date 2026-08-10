"""
stone game iv

topics:
dynamic programming - memoization
zero sum game, two player game, minimax

"""

class Solution:
    def alice(self, n, moves, outcome_memo):
        if n in outcome_memo:
            return outcome_memo[n]
        outcome = False
        for i in moves:
            if i>n:
                break
            elif i == n:
                outcome_memo[n] = True
                return True
            outcome =  (outcome or self.bob(n-i, moves, outcome_memo))
            if outcome:
                outcome_memo[n] = True
                return outcome
        outcome_memo[n] = False
        return outcome

    def bob(self, n, moves, outcome_memo):
        if n in outcome_memo:
            return not outcome_memo[n]
        outcome = True
        for i in moves:
            if i>n:
                break
            if i == n:
                outcome_memo[n] = True
                return False
            outcome = (outcome and self.alice(n-i, moves, outcome_memo))
            if not(outcome):
                outcome_memo[n] = True
                return outcome
        outcome_memo[n] = False
        return outcome

    def winnerSquareGame(self, n: int) -> bool:
        moves = []
        for i in range(1, floor(sqrt(n))+1):
            if i**2 <=n:
                moves.append(i**2)
        outcome_memo = {}
        return self.alice(n, moves, outcome_memo)

"""
Optimal Solution

@cache
def rec(i):
    if i == 0: return False

    for j in range(isqrt(i), 0, -1):
        if not rec(i-j**2): return True #any one of the recursive lower cases should be loss
    return False
ar = [rec(i) for i in range(100001)]

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return ar[n]
@cache
def rec(i):
    if i == 0: return False

    for j in range(isqrt(i), 0, -1):
        if not rec(i-j**2): return True #any one of the recursive lower cases should be loss
    return False
ar = [rec(i) for i in range(100001)]

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return ar[n]


"""