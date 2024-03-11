from typing import Optional
from copy import deepcopy
import time
from model.endMenu import EndMenu
from model.mainMenu import MainMenu
from view.viewMainMenu import ViewMainMenu
from .controller import Controller, Command
from model.button import Button
from view.viewEndMenu import ViewEndMenu
from AI.ai import AI, AIS

class GameController(Controller):

    def __init__(self, state, view):
        super().__init__(state, view)
        self.state.time = time.time()

    def handle_pressed_button(self, button: Button) -> Optional[Command]:
        action = button.get_action()

        if action == "Quit":
            self.state = MainMenu()
            self.view = ViewMainMenu(self.view.get_screen())
            return Command.CHANGE_MAIN
        
        if action == "Help":
            if self.state.selected_button is not None:  # Caso se ele clockou no Help mas ja tinha clickado anted 
                return None
            
            level_copy = deepcopy(self.state)
            ai = AI(level_copy, AIS.ASTARW, 1, 2000)
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
        dir = move.split()[0]
        indx = int(move.split()[1])

        self.state.unselect_button()    # o bolinho deseparece
        self.state.increment_score()

        if dir == "right":
            self.state.move_row(indx, 1, False)
        elif dir == "left":
            self.state.move_row(indx, -1, False)
        elif dir == "up":
            self.state.move_col(indx, -1, False)
        elif dir == "down":
            self.state.move_col(indx, 1, False)

