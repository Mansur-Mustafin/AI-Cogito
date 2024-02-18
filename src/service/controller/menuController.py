import pygame, sys
from typing import Optional
from .controller import Controller, Command
from abc import ABC, abstractmethod
from view.viewGame import ViewGame
from view.viewLevelMenu import ViewLevelMenu
from model.levelMenu import LevelMenu
from model.level import Level
from model.button import Button


class MenuController(Controller, ABC):

    def __init__(self, state, view):
        super().__init__(state, view)
    
    """
    Handles user events while in the menu such as quitting, mouse motion, and mouse button clicks
    :return: a command to be executed or None if no significant event has occur
    :rtype: Optional[Command]
    """
    def handle_event(self)-> Optional[Command] :
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.WINDOWCLOSE:
                print("QUIT")
                return Command.EXIT
            
            elif event.type == pygame.MOUSEMOTION:
                self.state.update_mouse_position(event.pos)
                return None

            elif event.type == pygame.MOUSEBUTTONDOWN:
                button = self.state.getPressedButton()

                if button is None : return None
                else: return self.hadle_pressed_button(button)
    @abstractmethod
    def hadle_pressed_button(self, button):
        pass




class MainMenuController(MenuController):

    def __init__(self, state, view):
        super().__init__(state, view)

    """
    Handles press buttons, changes state and view depending of the Menu option chosen
    :param button: Button that was pressed
    :type button: Button
    :return: a command to be executed
    :rtype: Optional[Command] 
    """
    def hadle_pressed_button(self, button:Button) -> Optional[Command]: # TODO change later when all option have been implemented
        if str(button) == "Jogar":
            self.state = LevelMenu()
            self.view = ViewLevelMenu(self.view.getScreen())
            return Command.CHANGE_LEVEL
        else: 
            print("TODO: ", button)
            return None




class LevelMenuController(MenuController):

    def __init__(self, state, view):
        super().__init__(state, view)
    """
    Handles press buttons, changes state and view depending of the Menu option chosen
    :param button: Button that was pressed
    :type button: Button
    :return: a command to be executed
    :rtype: Command]
    """
    def hadle_pressed_button(self, button:Button) -> Command:
        lvl = str(button).split(' ')[1]
        self.state = Level(lvl)
        self.view = ViewGame(self.view.getScreen())
        return Command.CHANGE_GAME
