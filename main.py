import pygame
# Initialisation de Pygame
pygame.init()
clock = pygame.time.Clock()

#constants

speed = 4
unitySize = 32
tick = unitySize//speed
fps =15

width = 15
height = 15

snakeWidth =28

class Player:

    def __init__(self):
        self.x = 3*unitySize + (unitySize - snakeWidth)/2
        self.y = (height//2)*unitySize + (unitySize - snakeWidth)/2
        self.direction =(0,0)
        self.isEating = False
        self.surface = pygame.Surface((snakeWidth, snakeWidth))
        self.surface.fill((255, 0, 0))
        self.isDead = False
        
    def move(self):
        self.x += self.direction[0]*speed
        self.y += self.direction[1]*speed
        
        if(self.x <0 or self.x>width*unitySize - snakeWidth or self.y <0 or self.y> height*unitySize-snakeWidth):
            print("OKKKKK")
            self.isDead = True
        
    def render(self):
        screen.blit(self.surface, (self.x, self.y))


# Paramètres de la fenêtre
screen = pygame.display.set_mode((width*unitySize, height*unitySize))
pygame.display.set_caption("Snake")


#background screen
background = pygame.Surface((width*unitySize, height*unitySize))
lightGreen = (164,213,164)
darkGreen = (111,171,111)
for y in range(0, height):
    for x in range(0, width):
        if (x + y) % 2 == 0:
            pygame.draw.rect(background, lightGreen, (x*unitySize, y*unitySize, unitySize, unitySize))
        else:
            pygame.draw.rect(background, darkGreen, (x*unitySize, y*unitySize, unitySize, unitySize))

screen.blit(background, (0,0))

#snake
myPlayer = Player()
# Boucle de jeu
running = True

counter = 0
chosen = False
futureDirection = (0,0)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if counter == tick:
        chosen = False
        counter = 1
        myPlayer.direction = futureDirection
        
    else:
        counter+=1
    
        if chosen == False and counter != tick:
            keys = pygame.key.get_pressed()
            if myPlayer.direction[0] ==0:
                if keys[pygame.K_LEFT]:
                    futureDirection = (-1,0)
                    chosen = True
                if keys[pygame.K_RIGHT]:
                    futureDirection = (1,0)
                    chosen = True
            if myPlayer.direction[1] == 0:
                if keys[pygame.K_UP]:
                    futureDirection = (0,-1)
                    chosen = True
                if keys[pygame.K_DOWN]:
                    futureDirection = (0,1)
                    chosen = True
        
    myPlayer.move()
    screen.blit(background, (0, 0))
    myPlayer.render()
    if (myPlayer.isDead):
        pygame.quit()
    
    
    pygame.display.flip()
    clock.tick(fps)

# Quitter Pygame
pygame.quit()
