from typing import Optional

import pygame

from .controller import Controller, Command
from model.button import Button

class GameController(Controller):

    def __init__(self, state, view):
        super().__init__(state, view)

    def handle_pressed_button(self, button: Button) -> Optional[Command]:
        print(button.get_action())
        self.process_move(button.get_action())
        if self.state.is_win_condition():
            print("End Game")
            return Command.CHANGE_END   # TODO
        return None


    def process_move(self, move: str) -> None:
        dir = move.split()[0]
        indx = int(move.split()[1])

        if self.__is_valid_move(dir, indx):
            print("Valid move")
            self.state.increment_score()
            
            if dir == "right":
                return self.state.move_right(indx)
            elif dir == "left":
                return self.state.move_left(indx)
            elif dir == "up":
                return self.state.move_up(indx)
            elif dir == "down":
                return self.state.move_down(indx)
            else:
                print("[ERROR] Invalid move")
                return False
        else:
            print("Invalid move")


    def __is_valid_move(self, dir : str, indx : int) -> bool:
        if dir == "right":
            return self.state.get_value_at(indx, -1) != self.state.get_main_color()
        elif dir == "left":
            return self.state.get_value_at(indx, 0) != self.state.get_main_color()
        elif dir == "up":
            return self.state.get_value_at(0, indx) != self.state.get_main_color()
        elif dir == "down":
            return self.state.get_value_at(-1, indx) != self.state.get_main_color()
        else:
            print("[ERROR] Invalid move")
            return False
