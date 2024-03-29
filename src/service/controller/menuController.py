from typing import Optional
from model.mainMenu import MainMenu
from model.endMenu import EndMenu
from model.button import Button
from model.level import Level
from model.levelMenu import LevelMenu
from view.viewGame import ViewGame
from view.viewMainMenu import ViewMainMenu
from view.viewLevelMenu import ViewLevelMenu
from .controller import Controller, Command


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
        self.state = LevelMenu(None if ai_algorithm == "Play" else ai_algorithm)
        self.view = ViewLevelMenu(self.view.get_screen())
        return Command.CHANGE_LEVEL


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
        self.state = Level(lvl, ai_algorithm)
        self.view = ViewGame(self.view.get_screen())
        if ai_algorithm is None:
            return Command.CHANGE_GAME_PLAYER
        else:
            return Command.CHANGE_GAME_PC


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
