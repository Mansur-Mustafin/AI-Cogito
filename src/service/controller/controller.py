from abc import ABC, abstractmethod
from enum import Enum, auto

import pygame

from view.view import View


class Controller(ABC):
    KEY_DIRECTIONS = {
        pygame.K_UP: (0, -1),
        pygame.K_LEFT: (-1, 0),
        pygame.K_RIGHT: (1, 0),
        pygame.K_DOWN: (0, 1),
    }

    def __init__(self, state, view):
        self.state = state
        self.view = view

    @abstractmethod
    def handle_event(self):
        pass

    def get_view(self) -> View:
        return self.view

    def get_state(self) -> any:
        return self.state

    def update_screen(self):
        self.view.draw_screen(self.state)
        pygame.display.update()


class Command(Enum):
    EXIT = auto()
    CHANGE_GAME = auto()
    CHANGE_MAIN = auto()
    CHANGE_LEVEL = auto()
