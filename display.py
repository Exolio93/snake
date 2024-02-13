class powershellScreen:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        None
    
    def display(self,player, apple):
        L = [['*' for x in range(self.width)] for y in range(self.height)]
        appx,appy =apple.position
        L[appy][appx] = '@'
        L[player.positions[0][1]][player.positions[0][0]] = '0'
        for x,y in player.positions[1:]:
            L[y][x] = 'O'
        for y in range(self.height):
            for x in range(self.width):
                print(L[y][x], end= " ")
            print("")
        return L