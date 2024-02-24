from .controller import Controller
from model.button import Button
from typing import Optional
from controller.controller import Command
import time
from settings import WAITTING_TIME
from AI.ai import AI
from model.endMenu import EndMenu
from view.viewEndMenu import ViewEndMenu

class AIController (Controller):

    def __init__(self, state:AI, view):
        super().__init__(state, view)

    def handle_event(self) -> Optional[Command]:
        if(self.state.state.is_win_condition()):
            self.state = EndMenu(self.get_state())
            self.view = ViewEndMenu(self.view.get_screen())
            return Command.CHANGE_END
        move = self.state.getMove()
        time.sleep(WAITTING_TIME)
        self.process_move(move)
        return None

    def process_move(self, move: str) -> None:
        dir = move.split()[0]
        indx = int(move.split()[1])

        if self.state.state.is_valid_move(dir, indx):
            self.state.state.increment_score()

            if dir == "right":
                self.state.move_right(indx)
            elif dir == "left":
                self.state.move_left(indx)
            elif dir == "up":
                self.state.move_up(indx)
            elif dir == "down":
                self.state.move_down(indx)