from apple import Apple

class Player:
    def __init__(self,w, h, x_init,y_init):
        self.xInit = x_init
        self.yInit = y_init
        self.height = h
        self.width = w
        self.positions = [(x_init,y_init)]
        self.direction = (1,0)
        self.length = 1
        
    def reset(self):
        self.positions = [(self.xInit,self.yInit)]
        self.direction = (1,0)
        self.length = 1
    
    def move(self, isEating):
        newX = self.positions[0][0] + self.direction[0]
        newY = self.positions[0][1] + self.direction[1]
        self.positions.insert(0,(newX,newY))
        if not isEating:
            self.positions.pop()
        else:
            self.length += 1
    def bodyColision(self):
        newX = self.positions[0][0] + self.direction[0]
        newY = self.positions[0][1] + self.direction[1]
        
        if((newX,newY) in self.positions):
            return True
        return False        
            
    def wallColision(self):
        newX = self.positions[0][0] + self.direction[0]
        newY = self.positions[0][1] + self.direction[1]
        if newX<0 or newX>=self.width or newY<0 or newY>=self.height:
            return True
        return False
    
    def deathCheck(self):
        if self.bodyColision() or self.wallColision():
            return True
        return False
    
    def willEat(self, apple):
        newX = self.positions[0][0] + self.direction[0]
        newY = self.positions[0][1] + self.direction[1]
        x,y = apple.position
        
        if x==newX and y==newY:
            return True
        return False