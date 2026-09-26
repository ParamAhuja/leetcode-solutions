class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        k = {}
        for i in knowledge:
            k[i[0]] = i[1]
        
        

        i = 0
        n = len(s)
        ans = ""
        while(i<n):
            if s[i] == "(":
                temp = ""
                i+=1
                while(s[i]!=")"):
                    temp+=s[i]
                    i+=1
                if temp not in k:
                    ans+="?"
                else:
                    ans+=k[temp]
            else:
                ans+=s[i]
            i+=1
        return ans