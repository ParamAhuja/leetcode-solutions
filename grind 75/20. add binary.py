
"""
full adder logic in addDigits
Ripple adder in addBinary - keep adding a, b, c until any of them is >0
"""

class Solution:
    def addDigits(self, a, b, c):
        AB_xor = (a and not b) or (not a and b)
        AB = a and b

        carryOut = (AB_xor and c) or AB
        sum = (AB_xor and not c) or (not AB_xor and c) 

        return int(sum), int(carryOut)

    def addBinary(self, a: str, b: str) -> str:
        # sum = xor
        # carry = and

        ans = []

        carryIn = 0
        i = len(a)-1
        j = len(b)-1
        while i>=0 or j>=0 or carryIn:
            if i>=0:
                n1 = a[i]
                i-=1
            else:
                n1 = 0
            
            if j>=0:
                n2 = b[j]
                j-=1
            else:
                n2 = 0
            
            sum, carryIn = self.addDigits(bool(int(n1)), bool(int(n2)), bool(int(carryIn)))
            ans.insert(0, str(sum))
        return "".join(ans)