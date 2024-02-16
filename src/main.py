import pygame, sys
from settings import *

from analitics import *

from view.viewGame import ViewGame
from view.viewLevelMenu import ViewLevelMenu
from view.viewMainMenu import ViewMainMenu

from model.mainMenu import MainMenu
from model.levelMenu import LevelMenu
from model.level import Level

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
        
        self.controller = MainMenuController(MainMenu(), ViewMainMenu(self.screen))


    def run(self):
        run = True
        while run:

            command = self.controller.handle_event()
            run = self.handle_command(command)
            
            self.controller.getView().draw_screen(self.controller.getState())

            pygame.display.update()
            self.clock.tick(FPS)

        self.quit()


    def handle_command(self, command):
        if command is None:
            return True
        
        if command == Controller.EXIT:
            return False
        
        state = self.controller.getState()
        view = self.controller.getView()

        if command == Controller.CHANGE_GAME:
            self.controller = GameController(state, view)
        elif command == Controller.CHANGE_MAIN:
            self.controller = MainMenuController(state, view)
        elif command == Controller.CHANGE_LEVEL:
            self.controller = LevelMenuController(state, view)
        else:
            print("TODO")
        return True


    def quit(self):
        pygame.quit()
        sys.exit()



if __name__ == "__main__":
    game = Game()
    game.run()