import sys

import pygame

from AI.ai import *
from model.mainMenu import MainMenu
from service.controller.aiController import AIController
from service.controller.gameController import GameController
from service.controller.menuController import EndMenuController, HueristicMenuController, LevelMenuController, MainMenuController
from view.viewMainMenu import ViewMainMenu


class Game:
    """
    This class represents the main game class for 'Cogito Game'.
    Handling the initialization, game loop, controller management, and screen updates.
    """

    def __init__(self) -> None:
        """
        Initialize the game.

        Attributes:
        ----------
            screen (pygame.Surface): The display surface for rendering the game.
            clock (pygame.time.Clock): Clock used for controlling the frame rate.
            controller (Controller): The initial controller managing the game state, set to MainMenuController.
            command_actions (dict): A mapping of command enums to their corresponding action functions.
        """
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption('Cogito Game')
        self.clock = pygame.time.Clock()

        # controller
        self.controller = MainMenuController(MainMenu(), ViewMainMenu(self.screen))

        # actions to change controller
        self.command_actions = {
            Command.EXIT: lambda: False,
            Command.CHANGE_GAME_PLAYER: lambda: self.change_controller(GameController),
            Command.CHANGE_GAME_PC: lambda: self.change_controller(AIController),
            Command.CHANGE_MAIN: lambda: self.change_controller(MainMenuController),
            Command.CHANGE_LEVEL: lambda: self.change_controller(LevelMenuController),
            Command.CHANGE_END: lambda: self.change_controller(EndMenuController),
            Command.CHANGE_HUERISTIC: lambda: self.change_controller(HueristicMenuController)
        }

    def run(self):
        """
        Starts the main game loop. Continuously processes events and updates the current controller.

        :return: None
        """
        run = True
        while run:
            command = self.controller.handle_event()
            run = self.handle_command(command)
            self.controller.update_screen()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

    def handle_command(self, command):
        """
        Processes a command received from the current controller
        :param command: The command received from the controller.
        :type command: Command Class
        :return: A boolean indicating whether the game should continue running.
        :rtype: bool
        """
        action = self.command_actions.get(command, lambda: True)  # if not found: run = True
        return action()

    def change_controller(self, controller_class):
        """
        Changes the current controller of the game.
        :param controller_class: The class of the new controller to be instantiated.
        :type controller_class: Controller Class
        :return: Always True
        :rtype: bool
        """
        self.controller = controller_class(self.controller.get_state(), self.controller.get_view())
        return True
