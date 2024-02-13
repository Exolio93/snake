import numpy as np

from tf_agents.environments import py_environment as pye
from tf_agents.environments import tf_environment as tfe
from tf_agents.trajectories import time_step as ts
from tf_agents.specs import array_spec
from tf_agents.environments import tf_py_environment
from tf_agents.environments import utils
from tf_agents.environments import wrappers
from tf_agents.environments import suite_gym
from tf_agents.trajectories import time_step as ts

from apple import Apple
from player import Player

height = 15
width = 15
xInit = 2
yInit = 5

class snakeEnv(pye.PyEnvironment): #snakeEnv est une sous-classe de pyEnvironment
    
    def getObservation(self):
        L = [0 for _ in range(self.w*self.h + 2)]
        L[0] = self.player.direction[0]
        L[1] = self.player.direction[1]
                
        appx,appy =self.apple.position
        
        L[appy*self.w + appx + 2] = -1
        for i in range(len(self.player.positions)):
            x,y = self.player.positions[i]
            L[y*self.w + x + 2] = i+1
        return np.array(L,dtype=np.int32)
    
    def __init__(self,height, width, xInit, yInit):
        
        self.h = height
        self.w = width
        
        self.player = Player(width, height, xInit, yInit)
        self.apple = Apple(width, height)
        self.apple.replace(self.player)

        self._action_spec = array_spec.BoundedArraySpec(shape=(), dtype=np.int32, minimum=-1, maximum=1, name='action')
        self._observation_spec = array_spec.BoundedArraySpec(shape=(3,), dtype=np.int32, minimum=-1, maximum = 500,name='observation')       
        self._state = np.zeros(3,dtype=np.int32).reshape((3,))
        self._episode_ended = False
        
    def getGamma(self):
        n = self.player.length
        return n/(self.h*self.w)
         
    def displayMap(self):
        L = [['*' for x in range(self.w)] for y in range(self.h)]
        appx,appy =self.apple.position
        L[appy][appx] = '@'
        L[self.player.positions[0][1]][self.player.positions[0][0]] = '0'
        for x,y in self.player.positions[1:]:
            L[y][x] = 'O'
        for y in range(self.h):
            for x in range(self.w):
                print(L[y][x], end= " ")
            print("")
        return L
    
    # def showGame(self, AI): 
    #     self.displayMap()
    #     while True:
    #         input()
    #         direction = AI.choseDirection(self.getMap())
    #         print(self.player.positions)
    #         (x,y) = self.player.direction
    #         if direction == "turnLeft":
    #             player.direction = (y,-x)
    #         if direction == "turnRight":
    #             player.direction = (-y,x)
                            
    #         if self.player.deathCheck():
    #             print("FINISHED")
    #             break;
    #         if self.player.willEat(self.apple):
    #             self.player.move(True)
    #             self.player.length += 1
    #             self.apple.replace(self.player)
    #         else:
    #             self.player.move(False)
    #         print(self.getMap())
    #         #self.displayMap()
    
    def action_spec(self):
        return self._action_spec

    def observation_spec(self):
        return self._observation_spec

    def _reset(self):
        self.player.reset()
        self.apple.replace(self.player)
        #self._state = np.zeros((3,1),dtype=np.int32)
        self._episode_ended = False
        return ts.restart(np.array([self._state], dtype=np.int32))
    
    def _step(self, action):
        if self._episode_ended:
            return self.reset()
        
        #capture de la direction
        (x,y) = self.player.direction
        if action == -1:
            self.player.direction = (y,-x)
        elif action == 1:
            self.player.direction = (-y,x)
            
        #test de mort
        if self.player.deathCheck():
            self._episode_ended = True
            return ts.termination(np.array([self._state], dtype=np.int32), reward = -1)
        
        # Effecteur le mouvement
        reward = 0
        if self.player.willEat(self.apple):
            reward += 1
            self.player.move(True)
            self.player.length += 1
            self.apple.replace(self.player)
        else:
            self.player.move(False)
            
        #test de récompense
        x,y = self.player.positions[0]
        appx,appy = self.apple.position
        dirx,diry = self.player.direction
        
        if abs(x-appx) + abs(y-appy) > abs(x+dirx-appx) + abs(y+diry-appy):
            reward += 0.1
        else:
            reward -= 0.1
            
           
        #self._state = np.zeros((3,1),dtype=np.int32)
        return ts.transition(np.array([self._state], dtype=np.int32), reward=reward, discount=self.getGamma())
            

myEnv = snakeEnv(height, width, xInit, yInit)
utils.validate_py_environment(myEnv, episodes=5)
