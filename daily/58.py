class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        s = s.rstrip()
        for i in range(len(s)-1, -1, -1):
            if s[i]==" ":
                break
            else:
                length+=1
        return length
