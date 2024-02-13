import numpy as np
from apple import Apple
from display import powershellScreen
from inputs import Inputs
from player import Player
height = 15
width = 15
x_init = 2
y_init = 5
 
                            
screen = powershellScreen(height, width)
myInputs = Inputs()

player = Player(width, height, x_init, y_init)
apple = Apple(width, height)
apple.replace(player)

screen.display(player,apple)
while True:
    direction = Inputs.catch()
    x,y = player.direction

    if player.direction[0] == 0:
        if direction == "left":
            player.direction = (-1,0)
        if direction == "right":
            player.direction = (1,0)
    if player.direction[1] == 0:
        if direction == "top":
            player.direction = (0,-1)
        if direction == "bottom":
            player.direction = (0,1)

    if player.deathCheck():
        print("YOU LOST !")
        break;
    if player.willEat(apple):
        player.move(True)
        apple.replace(player)
    else:
        player.move(False)
    screen.display(player,apple)

# class snakeForAI:
    
#     def __init__(self):
#         self.player = Player(width, height, x_init, y_init)
#         self.apple = Apple(width, height)
#         self.apple.replace(self.player)

#     def reset(self):
#         self.player.reset()
#         self.apple.replace(self.player)

#     def getObservation(self):
#         L = [0 for _ in range(width*height + 2)]
#         L[0] = self.player.direction[0]
#         L[1] = self.player.direction[1]
                
#         appx,appy =self.apple.position
        
#         L[appy*width + appx + 2] = -1
#         for i in range(len(self.player.positions)):
#             x,y = self.player.positions[i]
#             L[y*width + x + 2] = i+1
#         return np.array(L)
    
#     def displayMap(self):
#         L = [['*' for x in range(width)] for y in range(height)]
#         appx,appy =self.apple.position
#         L[appy][appx] = '@'
#         L[self.player.positions[0][1]][self.player.positions[0][0]] = '0'
#         for x,y in self.player.positions[1:]:
#             L[y][x] = 'O'
#         for y in range(height):
#             for x in range(width):
#                 print(L[y][x], end= " ")
#             print("")
#         return L
    
#     def showGame(self, AI): 
#         self.displayMap()
#         while True:
#             input()
#             direction = AI.choseDirection(self.getMap())
#             print(self.player.positions)
#             (x,y) = self.player.direction
#             if direction == "turnLeft":
#                 self.player.direction = (y,-x)
#             if direction == "turnRight":
#                 self.player.direction = (-y,x)
                            
#             if self.player.deathCheck():
#                 print("FINISHED")
#                 break;
#             if self.player.willEat(self.apple):
#                 self.player.move(True)
#                 self.player.length += 1
#                 self.apple.replace(self.player)
#             else:
#                 self.player.move(False)
#             print(self.getMap())
#             #self.displayMap()

#     def fitness(self,AI):   
#         nActions = 0
#         nApples = 0
#         gettingClose = 0
#         while nActions <= 2000:
#             nActions += 1
#             direction = AI.choseDirection(self.getMap())
#             if self.player.direction[0] == 0:
#                 if direction == "left":
#                     self.player.direction = (-1,0)
#                 if direction == "right":
#                     self.player.direction = (1,0)
#             if self.player.direction[1] == 0:
#                 if direction == "top":
#                     self.player.direction = (0,-1)
#                 if direction == "bottom":
#                     self.player.direction = (0,1)
#             x,y = self.player.positions[0]
#             appx,appy = self.apple.position
#             dirx,diry = self.player.direction
            
#             if abs(x-appx) + abs(y-appy) > abs(x+dirx-appx) + abs(y+diry-appy):
#                 gettingClose += 0.1
#             else:
#                 gettingClose -= 0.1
                 
#             if self.player.deathCheck():
#                 break;
#             if self.player.willEat(self.apple):
#                 nApples +=1
#                 self.player.move(True)
#                 self.apple.replace(self.player)
#             else:
#                 self.player.move(False)
#         fit = nApples + gettingClose
#         return fit
        
