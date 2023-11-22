class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        ptr=[(0,1),(1,0),(0,-1),(-1,0)]
        x,y=0,0
        dir=0
        for i in instructions:
            if i=="G":
                x=x+ptr[dir][0]
                y=y+ptr[dir][1]
            if i=="R":
                dir=(dir+1)%4
            if i =="L":
                dir=(dir-1)%4
        return (x==0 and y==0) or dir!=0
