from typing import Optional
from model.mainMenu import MainMenu
from model.endMenu import EndMenu
from model.button import Button
from model.level import Level
from model.levelMenu import LevelMenu
from model.heuristicMenu import HeuristicMenu
from view.viewGame import ViewGame
from view.viewMainMenu import ViewMainMenu
from view.viewLevelMenu import ViewLevelMenu
from view.viewHeuristicMenu import ViewHeuristicMenu
from .controller import Controller, Command
from AI.ai import AIS
from settings import *

class MainMenuController(Controller):

    def __init__(self, state, view):
        super().__init__(state, view)

    def handle_pressed_button(self, button: Button) -> Optional[Command]:
        """
        Handles press buttons, changes state and view depending on the Menu option chosen
        :param button: Button that was pressed
        :type button: Button
        :return: a command to be executed
        :rtype: Optional[Command]
        """
        ai_algorithm = button.get_action()
        if ai_algorithm == "Play":
            self.state = LevelMenu(None)
            self.view = ViewLevelMenu(self.view.get_screen())
            return Command.CHANGE_LEVEL
        elif ai_algorithm in [AIS.DFS, AIS.BFS, AIS.IDS]:
            self.state = LevelMenu(ai_algorithm)
            self.view = ViewLevelMenu(self.view.get_screen())
            return Command.CHANGE_LEVEL
        elif ai_algorithm in [AIS.GREDDY, AIS.ASTAR, AIS.ASTARW]:
            self.state = HeuristicMenu(ai_algorithm)
            self.view = ViewHeuristicMenu(self.view.get_screen())
            return Command.CHANGE_HUERISTIC


class LevelMenuController(Controller):

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
        ai_algorithm = self.state.ai_algorithm
        heuristic = self.state.heuristic
        self.state = Level(lvl, ai_algorithm, heuristic)
        self.view = ViewGame(self.view.get_screen())
        if ai_algorithm is None:
            return Command.CHANGE_GAME_PLAYER
        else:
            return Command.CHANGE_GAME_PC


class HueristicMenuController(Controller):

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
        heuristic = button.get_action()
        self.state = LevelMenu(self.state.ai_algorithm, heuristic)
        self.view = ViewLevelMenu(self.view.get_screen())
        return Command.CHANGE_LEVEL


class EndMenuController (Controller):
        
    def __init__(self, state: EndMenu, view):
        super().__init__(state, view)

    def handle_pressed_button(self, button: Button) -> Command | None:
        """
        Handles press buttons, changes state and view depending of the Menu option chosen
        :param button: Button that was pressed
        :type button: Button
        :return: a command to be executed
        :rtype: Command]
        """
        assert type(self.state) is EndMenu
        if button.get_action() == "Play Again":
            self.state = Level(self.state.level.level)
            self.view = ViewGame(self.view.get_screen())
            return Command.CHANGE_GAME_PLAYER
        elif button.get_action() == "Go back to menu":
            self.state = MainMenu()
            self.view = ViewMainMenu(self.view.get_screen())
            return Command.CHANGE_MAIN
        return None
