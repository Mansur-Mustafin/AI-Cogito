from typing import Optional
import time
from model.endMenu import EndMenu
from model.mainMenu import MainMenu
from view.viewMainMenu import ViewMainMenu
from .controller import Controller, Command
from model.button import Button
from view.viewEndMenu import ViewEndMenu


class GameController(Controller):

    def __init__(self, state, view):
        super().__init__(state, view)
        self.state.time = time.time()

    def handle_pressed_button(self, button: Button) -> Optional[Command]:
        if button.get_action() == "Quit":
            self.state = MainMenu()
            self.view = ViewMainMenu(self.view.get_screen())
            return Command.CHANGE_MAIN

        self.process_move(button.get_action())
        if self.state.is_win_condition() or self.state.lost():
            self.state.time = time.time() - self.state.time
            self.state = EndMenu(self.get_state())
            self.view = ViewEndMenu(self.view.get_screen())
            return Command.CHANGE_END

        return None

    def process_move(self, move: str) -> None:
        dir = move.split()[0]
        indx = int(move.split()[1])

        #if self.state.is_valid_move(dir, indx):
        self.state.increment_score()

        if dir == "right":
            self.state.move_row(indx, 2, True)
        elif dir == "left":
            self.state.move_row(indx, -2, True)
        elif dir == "up":
            self.state.move_col(indx, -2, True)
        elif dir == "down":
            self.state.move_col(indx, 2, True)

