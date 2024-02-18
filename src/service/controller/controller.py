from abc import ABC, abstractmethod
from enum import Enum, auto
import pygame, sys
from view.view import View

class Controller(ABC):

    KEY_DIRECTIONS = {
        pygame.K_UP :   (0, -1),
        pygame.K_LEFT : (-1, 0),
        pygame.K_RIGHT: (1, 0),
        pygame.K_DOWN:  (0, 1),
    }
    
    def __init__(self, state, view):
        self.state = state
        self.view = view 

    @abstractmethod
    def handle_event(self):
        pass
    
    def getView(self) -> View:
        return self.view

    def getState(self) -> any:
        return self.state
    

class Command(Enum):
    EXIT = auto()
    CHANGE_GAME = auto()
    CHANGE_MAIN = auto()
    CHANGE_LEVEL = auto()