"""
# todo again
"""

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        temp = ""
        ans = ""
        count_1 = 0
        for right in range(n):
            temp += s[right]
            temp = temp.lstrip("0")
            if s[right] == "1":
                count_1+=1
            if count_1 == k:
                if ans=="" or (len(ans)>len(temp)):
                    ans= temp
                elif len(ans)==len(temp):
                    ans = min(ans, temp)
                count_1-=1
                for i in range(len(temp)):
                    if temp[i]=="1":
                        temp = temp[i+1:]
                        break
        return ans