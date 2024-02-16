import pygame, sys
from settings import *
from model.level import Level
from view.viewGame import ViewGame
from view.viewMenu import ViewMenu
from model.menu import Menu

class Game:
    def __init__(self) -> None:

        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Amado Game')
        self.clock = pygame.time.Clock()
        
        # self.state = Level(2)
        # self.view = ViewGame(self.screen)
        self.state = Menu()
        self.view = ViewMenu(self.screen)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.view.draw_screen(self.state)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()