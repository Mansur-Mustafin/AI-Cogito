import pygame

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
        keys = pygame.key.get_pressed()
        for key, direction in self.KEY_DIRECTIONS.items():
            if keys[key]:
                return direction
        return (0, 0)

    def move(self):
        move = self.getMove()
        self.level.movePlayer(move)
        print(self.level.cur_pos)
        return self.level.isWinCondition()