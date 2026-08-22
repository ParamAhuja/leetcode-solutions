
"""
python specific:
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip() # this will take extra memory as it returns string
        if len(s) == 0:
            return 0
        i = 0
        if s[i] == "-":
            factor = -1
            i+=1
        elif s[i] == "+":
            factor = 1
            i+=1
        else:
            factor = 1
        ans = 0
        while( i<len(s) and s[i].isnumeric() ):
            ans*=10
            digit = int(s[i])
            ans+=digit
            i+=1
        ans*= factor
        lower_limit = -1*(2**31)
        upper_limit = (2**31)-1
        if ans <= lower_limit:
            return lower_limit
        if ans >= upper_limit:
            return upper_limit
        return ans


"""
explicit method for other langs:
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        # s = s.lstrip(" ") # this will take extra memory as it returns string
        while(i<len(s) and s[i].isspace()): # same time in constant memory
            i+=1
        if len(s)-i == 0:
            return 0
        if s[i] == "-":
            factor = -1
            i+=1
        elif s[i] == "+":
            factor = 1
            i+=1
        else:
            factor = 1
        ans = 0
        lower_limit = -214748364
        lower_digit = 8
        upper_limit = 214748364
        upper_digit = 7
        while( i<len(s) and s[i].isnumeric() ):
            temp = factor*ans
            digit = int(s[i])
            if (temp==lower_limit and digit>=lower_digit) or (temp<lower_limit):
                return -2**31
            elif (temp== upper_limit and digit>=upper_digit) or (temp> upper_limit):
                return 2**31-1
            ans*=10
            ans+=digit
            i+=1
        return factor * ans