class Solution:
    # walking robot simulation 1
    def move (self, dist, direction, h, x, y):
        if direction == 0:
            for i in range(dist):
                if (x, y+1) not in h:
                    y+=1
                else:
                    break

        elif direction==1:
            for i in range(dist):
                if (x+1, y) not in h:
                    x+=1
                else:
                    break

        elif direction==2:
            for i in range(dist):
                if (x, y-1) not in h:
                    y-=1
                else:
                    break

        elif direction==3:
            for i in range(dist):
                if (x-1, y) not in h:
                    x-=1
                else:
                    break
        return (x,y)
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        h = {}
        for i in obstacles:
            h[tuple(i)] = 1
        x = 0
        y = 0
        ans = -math.inf
        direction = 0
        for i in commands:
            if i == -1:
                direction = (direction+1)%4
            elif i == -2:
                direction = (direction-1)%4
            else:
                x, y = self.move(i, direction, h, x, y)
            ans = max(ans, x**2+y**2)
        return ans