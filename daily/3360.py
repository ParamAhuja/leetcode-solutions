class Solution:
    def canAliceWin(self, n: int) -> bool:
        # method 1: hardcode all:
        # <10 bob wins
        # 10-18 alice wins
        # 19-26 - bob wins
        # 27-33 - alice
        # 34 - 39 - bob
        # 40- 44 alice
        # 45-48 bob
        # 49-51 alice
        # 52, 53 - bob
        # 54<= alice

        # method 2: simulate:
        turn = 0
        r = 10
        while True:
            if n<r or r==0:
                return bool(turn)
            n-=r
            r-=1
            turn = 1-turn
