import random as r

class Apple:
    
    
    def __init__(self,w,h):
        self.width = w
        self.height = h
        self.position = None
        
    def replace(self,player):
        applePos = player.positions[0]
        while applePos in player.positions :
            applePos = r.randint(1,self.width-1), r.randint(1,self.height-1)
        self.position = applePos
       