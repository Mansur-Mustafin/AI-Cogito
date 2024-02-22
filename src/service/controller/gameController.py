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
        if self.state.is_win_condition():
            self.state.time = time.time() - self.state.time
            self.state = EndMenu(self.get_state())
            self.view = ViewEndMenu(self.view.get_screen())
            return Command.CHANGE_END
        return None

    def process_move(self, move: str) -> None:
        dir = move.split()[0]
        indx = int(move.split()[1])

        if self.__is_valid_move(dir, indx):
            self.state.increment_score()

            if dir == "right":
                self.state.move_right(indx)
            elif dir == "left":
                self.state.move_left(indx)
            elif dir == "up":
                self.state.move_up(indx)
            elif dir == "down":
                self.state.move_down(indx)


    def __is_valid_move(self, dir: str, indx: int) -> bool:
        if dir == "right":
            return not self.state.get_value_at(indx, -1) in self.state.get_main_colors()
        elif dir == "left":
            return not self.state.get_value_at(indx, 0) in self.state.get_main_colors()
        elif dir == "up":
            return not self.state.get_value_at(0, indx) in self.state.get_main_colors()
        elif dir == "down":
            return not self.state.get_value_at(-1, indx) in self.state.get_main_colors()
        else:
            print("[ERROR] Invalid move")
            return False
