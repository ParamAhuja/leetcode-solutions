class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        options = 3*(2**(n-1))
        if k>options:
            return ""
        ans = ""

        
        if k<=2**(n-1):
            ans+="a"
        elif k<=2**n:
            ans+="b"
            k-=2**(n-1)
        else:
            ans+="c"
            k-=2**(n)
        options -=2**n

        while (len(ans)<n):
            if k>options//2:
                choices = ["a", "b", "c"]
                choices.remove(ans[-1])
                ans+= choices[1]
                k-=options//2
                options//=2
            else:
                choices = ["a", "b", "c"]
                choices.remove(ans[-1])
                ans+= choices[0]
                options//=2
        return ans

            
