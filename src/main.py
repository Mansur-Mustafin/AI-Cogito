import pygame
import sys
from settings import *
from model.mainMenu import MainMenu
from service.controller.controller import Command
from service.controller.gameController import GameController
from service.controller.menuController import LevelMenuController
from service.controller.menuController import MainMenuController, EndMenuController
from view.viewMainMenu import ViewMainMenu


class Game:

    def __init__(self) -> None:
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Cogito Game')
        self.clock = pygame.time.Clock()

        # controller
        self.controller = MainMenuController(MainMenu(), ViewMainMenu(self.screen))

        # actions to change controller
        self.command_actions = {
            Command.EXIT: lambda: False,
            Command.CHANGE_GAME: lambda: self.change_controller(GameController),
            Command.CHANGE_MAIN: lambda: self.change_controller(MainMenuController),
            Command.CHANGE_LEVEL: lambda: self.change_controller(LevelMenuController),
            Command.CHANGE_END: lambda: self.change_controller( EndMenuController)
        }

    def run(self):
        run = True
        while run:
            command = self.controller.handle_event()
            run = self.handle_command(command)

            self.controller.update_screen()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

    def handle_command(self, command):
        action = self.command_actions.get(command, lambda: True)  # if not find: run = True
        return action()

    def change_controller(self, controller_class):
        self.controller = controller_class(self.controller.get_state(), self.controller.get_view())
        return True


if __name__ == "__main__":
    game = Game()
    game.run()
