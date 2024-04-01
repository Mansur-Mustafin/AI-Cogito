import time
from copy import deepcopy
from typing import Optional

from AI.ai import AI, AIS, H
from model.button import Button
from model.endMenu import EndMenu
from model.mainMenu import MainMenu
from view.viewEndMenu import ViewEndMenu
from view.viewMainMenu import ViewMainMenu
from .controller import Controller, Command


class GameController(Controller):
    """
    A controller class for handling game logic, including responding to button presses, managing game state changes.
    Inherits from Controller.
    """
    def __init__(self, state, view):
        """
        Initializes the GameController with the specified game state and view.
        :param state: The state of the game.
        :param view: The view of the game.
        """
        super().__init__(state, view)
        self.state.time = time.time()

    def handle_pressed_button(self, button: Button) -> Optional[Command]:
        """
        Handles actions triggered by button presses during gameplay.
        :param button: The button that was pressed.
        :return: Optional[Command]
        """
        action = button.get_action()

        if action == "Quit":
            self.state = MainMenu()
            self.view = ViewMainMenu(self.view.get_screen())
            return Command.CHANGE_MAIN

        if action == "Help":
            if self.state.selected_button is not None:  # Caso se ele clockou no Help mas ja tinha clickado anted 
                return None

            level_copy = deepcopy(self.state)
            ai = AI(level_copy, AIS.ASTARW, H.MANHATTAN_PATTERN, 1, 2000)
            move = ai.moves[0]
            self.state.select_button(move)
            return None

        self.process_move(action)
        if self.state.is_win_condition() or self.state.lost():
            self.state.time = time.time() - self.state.time
            self.state = EndMenu(self.get_state())
            self.view = ViewEndMenu(self.view.get_screen())
            return Command.CHANGE_END

        return None

    def process_move(self, move: str) -> None:
        """
        Processes a move by updating the game state accordingly.
        :param move: The move to be processed.
        :return: None
        """
        direction = move.split()[0]
        index = int(move.split()[1])

        self.state.unselect_button()  # o bolinho deseparece
        self.state.increment_score()

        if direction == "right":
            self.state.move_row(index, 1, False)
        elif direction == "left":
            self.state.move_row(index, -1, False)
        elif direction == "up":
            self.state.move_col(index, -1, False)
        elif direction == "down":
            self.state.move_col(index, 1, False)
