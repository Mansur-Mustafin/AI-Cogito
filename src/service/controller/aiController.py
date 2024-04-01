from typing import Optional

import pygame

from service.controller.controller import Controller
from AI.ai import AI
from model.mainMenu import MainMenu
from view.viewMainMenu import ViewMainMenu
from view.viewGame import ViewGame
from settings import *


class AIController(Controller):

    def __init__(self, state, view):
        super().__init__(state, view)

        assert isinstance(view, ViewGame), "view must be an instance of ViewGame"

        self.view.draw_waiting_for_ai()
        ai = AI(state, state.ai_algorithm, state.heuristic)
        self.ai_moves = ai.moves
        state.time = ai.state.time
        self.curr_move = 0
        pygame.time.set_timer(TIMER_EVENT, WAITING_TIME)

    def handle_event(self) -> Optional[Command]:
        if pygame.event.peek(TIMER_EVENT) and self.curr_move < len(self.ai_moves):
            pygame.event.clear(TIMER_EVENT)
            self.process_move(self.ai_moves[self.curr_move])
            self.curr_move += 1

        return super().handle_event()

    def process_move(self, move: str, opposite=False) -> None:
        dir = move.split()[0]
        indx = int(move.split()[1])

        self.state.increment_score()
        opposite_weight = -1 if opposite else 1
        if dir == "right":
            self.state.move_row(indx, opposite_weight * 1, False)
        elif dir == "left":
            self.state.move_row(indx, opposite_weight * -1, False)
        elif dir == "up":
            self.state.move_col(indx, opposite_weight * -1, False)
        elif dir == "down":
            self.state.move_col(indx, opposite_weight * 1, False)

    def handle_pressed_button(self, button):
        action = button.get_action()

        if action == "Quit":
            if not self.state.is_paused:
                pygame.time.set_timer(TIMER_EVENT, 0)
            self.state = MainMenu()
            self.view = ViewMainMenu(self.view.get_screen())
            return Command.CHANGE_MAIN
        elif action == "Next_left":
            if not self.state.is_paused:
                self.pause()
            if self.curr_move > 0:
                self.curr_move -= 1
                self.process_move(self.ai_moves[self.curr_move], True)
                self.state.score -= 2
        elif action == "Next_right":
            if not self.state.is_paused:
                self.pause()
            if self.curr_move < len(self.ai_moves):
                self.process_move(self.ai_moves[self.curr_move])
                self.curr_move += 1
        elif action == "Resume":
            if self.state.is_paused:
                self.unpause()
        elif action == "Pause":
            if not self.state.is_paused:
                self.pause()

        return None

    def pause(self):
        pygame.time.set_timer(TIMER_EVENT, 0)
        pygame.event.clear(TIMER_EVENT)
        self.state.pause()

    def unpause(self):
        pygame.time.set_timer(TIMER_EVENT, WAITING_TIME)
        self.state.unpause()
