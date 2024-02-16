from abc import ABC, abstractmethod
import pygame, sys


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
    
    def getView(self):
        return self.view

    def getState(self):
        return self.state
    

