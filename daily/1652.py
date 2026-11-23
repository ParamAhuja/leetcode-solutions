class ProductOfNumbers:

    def __init__(self):
        self.stream = deque()
        self.stream.append(1)
        self.lastZero = 0
        self.length = 0

    def add(self, num: int) -> None:
        self.length+=1
        if num==0:
            self.lastZero = self.length

            # RESET TO ZERO:
            self.stream = deque([1])

        else:
            self.stream.append(self.stream[-1]*num)

    def getProduct(self, k: int) -> int:
        # check if zero occured
        if (self.length-self.lastZero)<k:
            return 0
        else:
            return self.stream[-1] // self.stream[(-1*k)-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)