class Fancy:
    def __init__(self):
        self.a = []
        self.sum = 0
        self.prod = 1
        self.inverse = 1

    def append(self, val: int) -> None:
        val = (val-self.sum)*self.inverse
        self.a.append(val)

    def addAll(self, inc: int) -> None:
        self.sum+=inc

    def multAll(self, m: int) -> None:
        self.prod*=m
        self.sum*=m
        self.inverse = pow(self.prod,-1,10**9+7)

        
    def getIndex(self, idx: int) -> int:
        if idx>=len(self.a):
            return -1
        return (self.a[idx] * self.prod + self.sum)%(10**9+7)