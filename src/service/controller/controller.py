from abc import ABC, abstractmethod
from enum import Enum, auto
from .consts import *
import pygame

from view.view import View


class Controller(ABC):
    
    KEY_DIRECTIONS = {
        key: direction
        for direction_set, direction in zip([UP, LEFT, RIGHT, DOWN], [DIRECTION_UP, DIRECTION_LEFT, DIRECTION_RIGHT, DIRECTION_DOWN])
        for key in direction_set
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
