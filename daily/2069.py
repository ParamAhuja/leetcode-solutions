class Robot:
    # walking robot simulation 2
    def __init__(self, width: int, height: int):
        self.direction = {0: "East", 1: "North", 2: "West", 3: "South"}
        self.width = width
        self.height = height
        self.pos = [0,0]
        self.dir = 0

    def step(self, num: int) -> None:
        mod =  (2*self.width + 2*self.height - 4)
        if self.pos==[0,0] and num>=mod and num%mod==0:
            self.dir = 3
        num = num % mod
        if self.dir == 0:
            if self.pos[0]+num>self.width-1:
                a = self.pos[0]
                self.pos[0] = self.width-1
                self.dir = 1
                self.step(a+num - (self.width-1))
            else:
                self.pos[0]+=num
        elif self.dir == 1:
            if self.pos[1]+num>self.height-1:
                a = self.pos[1]
                self.pos[1] = self.height-1
                self.dir = 2
                self.step(a+num - (self.height-1))
            else:
                self.pos[1]+=num
        elif self.dir == 2:
            if self.pos[0]-num<0:
                a = self.pos[0]
                self.pos[0] = 0
                self.dir = 3
                self.step(num-a)
            else:
                self.pos[0]-=num
        else:
            if self.pos[1]-num<0:
                a = self.pos[1]
                self.pos[1] = 0
                self.dir = 0
                self.step(num-a)
            else:
                self.pos[1]-=num
        # print("pos after: ", self.pos)

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.direction[self.dir]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()