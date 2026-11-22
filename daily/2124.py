class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s)-1):
            if s[i]=="b" and s[i+1]=="a":
                return False
        return True

        # firstB = len(s)
        # for i in range(len(s)):
        #     if s[i]=="b":
        #         firstB = i
        #         break
        # lastA = -1
        # for i in range(len(s)-1, -1, -1):
        #     if s[i]=="a":
        #         lastA = i
        #         break
        # return firstB>lastA

        # firstB = s.find("b")
        # firstB = len(s) if firstB==-1 else firstB
        # lastA = s.rfind("a")
        # return firstB>lastA