class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:        

        direction = [[0,1], [1, 0], [0,-1], [-1, 0]]
        dir=['N','E','S','W']
        InitDirect = 0
        PosX = 0
        PosY = 0
        furthest = 0 

        x,y,d=0,0,0
        max_distance=0
        
        s=set((i,j) for i,j in obstacles)


        for num in commands:

            if num == -1:               
                InitDirect = (InitDirect + 1) % 4
            elif num == -2:
                InitDirect = (InitDirect - 1) % 4
            else:
                if dir[InitDirect]=='N':
                    for move in range(num):
                        if (x,y+1) in s:
                            break
                        y+=1
                elif dir[InitDirect]=='E':
                    for move in range(num):
                        if (x+1,y) in s:
                            break
                        x+=1
                elif dir[InitDirect]=='S':
                    for move in range(num):
                        if (x,y-1) in s:
                            break
                        y-=1
                else:
                    for move in range(num):
                        if (x-1,y) in s:
                            break
                        x-=1

                furthest = max(furthest, x ** 2 + y ** 2)
                    
        return furthest 

            


