from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Optional

import pygame

from view.view import View


class Command(Enum):
    EXIT = auto()
    CHANGE_GAME = auto()
    CHANGE_MAIN = auto()
    CHANGE_LEVEL = auto()
    CHANGE_END = auto()
    # AQUI

class Controller(ABC):

    def __init__(self, state, view):
        self.state = state
        self.view = view

    def handle_event(self) -> Optional[Command]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.WINDOWCLOSE:
                return Command.EXIT

            elif event.type == pygame.MOUSEMOTION:
                self.state.update_mouse_position(event.pos)
                return None

            elif event.type == pygame.MOUSEBUTTONDOWN:
                button = self.state.get_pressed_button()
                print("c")
                if button is None:
                    return None
                else:
                    return self.handle_pressed_button(button)

    @abstractmethod
    def handle_pressed_button(self, button):
        pass

    def get_view(self) -> View:
        return self.view

    def get_state(self) -> any:
        return self.state

    def update_screen(self):
        self.view.draw_screen(self.state)
        pygame.display.update()
