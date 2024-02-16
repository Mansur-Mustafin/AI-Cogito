import pygame, sys

class Controller:

    KEY_DIRECTIONS = {
        pygame.K_UP : (0, -1),
        pygame.K_LEFT : (-1,0),
        pygame.K_RIGHT: (1, 0),
        pygame.K_DOWN: (0, 1),
    }
    
    def __init__(self, level):
        self.level = level

    def getMove(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in self.KEY_DIRECTIONS:
                    return self.KEY_DIRECTIONS[event.key]
                else: return None
            
    
    def getLevel(self):
        return self.level

    def move(self):
        move = self.getMove()

        if move is None : return False

        self.level.movePlayer(move)
        print(self.level.cur_pos)
        return self.level.isWinCondition()