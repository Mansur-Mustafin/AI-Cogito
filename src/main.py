import pygame, sys
from settings import *
from model.level import Level
from view.viewGame import ViewGame
from view.viewLevelMenu import ViewLevelMenu
from view.viewMainMenu import ViewMainMenu
from model.mainMenu import MainMenu
from model.levelMenu import LevelMenu
from analitics import *
from controller.controller import Controller
from controller.gameController import GameController
from controller.menuController import MainMenuController
from controller.menuController import LevelMenuController

class Game:

    def __init__(self) -> None:

        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Amado Game')
        self.clock = pygame.time.Clock()
        
        self.state = LevelMenu()
        self.view = ViewLevelMenu(self.screen)

        self.controller = LevelMenuController(self.state, self.view)


    def run(self):
        run = True
        while run:

            run = not self.controller.handle_event()
            
            self.view.draw_screen(self.controller.getState())

            pygame.display.update()
            self.clock.tick(FPS)

        self.quit()

    def quit(self):
        pygame.quit()
        sys.exit()



if __name__ == "__main__":
    game = Game()
    game.run()