import pygame, sys
from settings import *

from service.analitics import *

from view.viewMainMenu import ViewMainMenu
from model.mainMenu import MainMenu

from service.controller.controller import Controller, Command
from service.controller.gameController import GameController
from service.controller.menuController import MainMenuController
from service.controller.menuController import LevelMenuController

class Game:

    def __init__(self) -> None:

        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Amado Game')
        self.clock = pygame.time.Clock()
        
        # controller
        self.controller = MainMenuController(MainMenu(), ViewMainMenu(self.screen))

        # actions to change controller
        self.command_actions = {
            Command.EXIT: lambda: False,
            Command.CHANGE_GAME: lambda: self.change_controller(GameController),
            Command.CHANGE_MAIN: lambda: self.change_controller(MainMenuController),
            Command.CHANGE_LEVEL: lambda: self.change_controller(LevelMenuController),
        }


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
        action = self.command_actions.get(command, lambda : True) # if not find just run = True
        return action()

    def change_controller(self, controller_class):
        self.controller = controller_class(self.controller.getState(), self.controller.getView())
        return True

    def quit(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()