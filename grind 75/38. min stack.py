class MinStack:

    def __init__(self):
        self.arr = []
        self.min = None 

    def push(self, value: int) -> None:
        if self.min == None or value<self.min:
            self.min = value
        self.arr.append([value, self.min ])

    def pop(self) -> None:
        if len(self.arr)!=0:
            mini = self.arr.pop()[0]
        
        if len(self.arr)!=0:
            self.min = self.arr[-1][1]
        else:
            self.min = None

        return mini
    
    def top(self) -> int:
        if len(self.arr)!=0:
            return self.arr[-1][0]

    def getMin(self) -> int:
        if len(self.arr)!=0:
            # print(self.arr[-1][0])
            # for i in self.arr:
            #     print("STACK: ")
            #     print(i)
            # print()
            return self.arr[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()