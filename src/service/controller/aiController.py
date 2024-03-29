from .controller import Controller, Command
from model.button import Button
from typing import Optional
import time
from settings import WAITING_TIME, TIMER_EVENT
from AI.ai import AI
from model.endMenu import EndMenu
from view.viewEndMenu import ViewEndMenu
from model.mainMenu import MainMenu
from view.viewMainMenu import ViewMainMenu
import pygame

class AIController (Controller):

    def __init__(self, state, view):
        super().__init__(state, view)
        ai = AI(state, state.ai_algorithm)
        self.ai_moves = ai.moves
        self.time = ai.state.time
        self.curr_move = 0
        pygame.time.set_timer(TIMER_EVENT, WAITING_TIME)

    def handle_event(self) -> Optional[Command]:
        if pygame.event.peek(TIMER_EVENT):
            pygame.event.clear(TIMER_EVENT)
            self.process_move(self.ai_moves[self.curr_move])
            self.curr_move += 1
            if self.curr_move == len(self.ai_moves):
                pygame.time.set_timer(TIMER_EVENT, 0)
                self.state = MainMenu()
                self.view = ViewMainMenu(self.view.get_screen())
                return Command.CHANGE_MAIN
            return None

        return super().handle_event

    def process_move(self, move: str) -> None:
        dir = move.split()[0]
        indx = int(move.split()[1])

        self.state.increment_score()

        if dir == "right":
            self.state.move_row(indx, 1, False)
        elif dir == "left":
            self.state.move_row(indx, -1, False)
        elif dir == "up":
            self.state.move_col(indx, -1, False)
        elif dir == "down":
            self.state.move_col(indx, 1, False)
    
    def handle_pressed_button(self, button):
        action = button.get_action()

        if action == "Quit":
            self.state = MainMenu()
            self.view = ViewMainMenu(self.view.get_screen())
            return Command.CHANGE_MAIN
        
        return None