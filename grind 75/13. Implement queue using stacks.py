

"""
# REVISE
METHOD 1: using queue_stack and temo_stack - 
 - O(1) for push O(N) for pop and peek OR
 - O(N) for push O(1) for pop and peek

OPTIMAL METHOD: using input(enqueue) and output(dequeue) stack
- amortized O(1) for both push and pop
"""

class MyQueue:

    def __init__(self):
        self.qs = [] # queue like stack
        self.ts = [] # temp stack

    def move(self, s1, s2):
        while(len(s1)!=0):
            s2.append( s1.pop() )

    def push(self, x: int) -> None:
        self.qs.append(x)

    def pop(self) -> int:
        if self.empty():
            return
        self.move(self.qs, self.ts)
        top = self.ts.pop()
        self.move(self.ts, self.qs)
        return top


    def peek(self) -> int:
        if self.empty():
            return
        self.move(self.qs, self.ts)
        top = self.ts[-1]
        self.move(self.ts, self.qs)
        return top

    def empty(self) -> bool:
        return len(self.qs) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


"""

amortized O(1) for push and pop

push operation:
push to input stack

pop operation:
if output is not empty, pop from there
else move all elements from input to output and then pop from there
# meaning, when output stack gets empty, it will be refilled with more elements to pop later, hence queue elements are split in both the stacks, hence amortized (to distribute)


class MyQueue:

    def __init__(self):
        self.inp = [] # queue like stack
        self.out = [] # temp stack

    def move(self, s1, s2):
        while(len(s1)!=0):
            s2.append( s1.pop() )

    def push(self, x: int) -> None:
        self.inp.append(x)

    def pop(self) -> int:
        if len(self.out)!=0:
            return self.out.pop()
        else:
            self.move(self.inp, self.out)
            return self.out.pop()


    def peek(self) -> int:
        if len(self.out)!=0:
            return self.out[-1]
        else:
            self.move(self.inp, self.out)
            return self.out[-1]

    def empty(self) -> bool:
        return (len(self.inp)+len(self.out)) == 0

"""