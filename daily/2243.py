class Solution:
    def digitSum(self, s: str, k: int) -> str:

        def digiSum(s):
            ans = 0
            for i in s:
                ans+= int(i)
            return str(ans)
            
        while len(s) > k: # do a round
            new_s = ""
            for i in range(0, len(s), k):
                new_s += digiSum(s[i: min(len(s), i+k)])
            s = new_s
        return s