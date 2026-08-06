class Solution:
    def prod(self, n):
        ans = 1
        while n!=0:
            ans*= n%10
            n//=10
        return ans
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            if self.prod(n)%t==0:
                return n
            n+=1
    
""" optimal: 
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        q, r = divmod(n, 10)
        
        req = t // gcd(max(q, 1), t)
        nxt = ((r + req - 1) // req) * req
        x = nxt - (nxt - 10) * (nxt // 10)

        return q * 10 + x
"""