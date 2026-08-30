# pow(x, n)

class Solution: # pow in O(logN)
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            return 1/self.myPow(x, -n)
            # or do myPow(1/x, -n)
        if n == 0:
            return 1
        if n == 1 or x == 0 or x==1:
            return x
        if n%2==0:
            a = self.myPow(x, n//2)
            return a*a
            # or do myPow(x*x, n//2)
        else:
            return x*self.myPow(x, n-1)