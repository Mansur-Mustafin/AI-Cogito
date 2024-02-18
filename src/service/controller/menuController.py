from abc import ABC, abstractmethod
from typing import Optional

import pygame

from model.button import Button
from model.level import Level
from model.levelMenu import LevelMenu
from view.viewGame import ViewGame
from view.viewLevelMenu import ViewLevelMenu
from .controller import Controller, Command


class MenuController(Controller, ABC):

    def __init__(self, state, view):
        super().__init__(state, view)

    def handle_event(self) -> Optional[Command]:
        """
        Handles user events while in the menu such as quitting, mouse motion, and mouse button clicks
        :return: a command to be executed or None if no significant event has occur
        :rtype: Optional[Command]
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.WINDOWCLOSE:
                print("QUIT")
                return Command.EXIT

            elif event.type == pygame.MOUSEMOTION:
                self.state.update_mouse_position(event.pos)
                return None

            elif event.type == pygame.MOUSEBUTTONDOWN:
                button = self.state.get_pressed_button()

                if button is None:
                    return None
                else:
                    return self.handle_pressed_button(button)

    @abstractmethod
    def handle_pressed_button(self, button):
        pass


class MainMenuController(MenuController):

    def __init__(self, state, view):
        super().__init__(state, view)

    def handle_pressed_button(self, button: Button) -> Optional[Command]:
        # TODO change later when all option have been implemented
        """
        Handles press buttons, changes state and view depending on the Menu option chosen
        :param button: Button that was pressed
        :type button: Button
        :return: a command to be executed
        :rtype: Optional[Command]
        """
        if str(button) == "Play":
            self.state = LevelMenu()
            self.view = ViewLevelMenu(self.view.get_screen())
            return Command.CHANGE_LEVEL
        else:
            print("TODO: ", button)
            return None


class LevelMenuController(MenuController):

    def __init__(self, state, view):
        super().__init__(state, view)

    def handle_pressed_button(self, button: Button) -> Command:
        """
        Handles press buttons, changes state and view depending of the Menu option chosen
        :param button: Button that was pressed
        :type button: Button
        :return: a command to be executed
        :rtype: Command]
        """
        lvl = str(button).split(' ')[1]
        self.state = Level(lvl)
        self.view = ViewGame(self.view.get_screen())
        return Command.CHANGE_GAME
