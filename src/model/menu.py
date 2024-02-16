from abc import ABC, abstractmethod
import pygame
from settings import *

class Menu(ABC):
    def __init__(self):
        self.mouse_pos = (WIDTH/2, HEIGHT/2)
        self.buttons = []
        
    def getButtons(self):
        return self.buttons
    
    def move_mouse(self, d_x, d_y):
        new_x = self.mouse_pos[0] + d_x
        new_y = self.mouse_pos[1] + d_y
        self.update_mouse_position(new_x, new_y)

    def update_mouse_position(self, new_x, new_y):
        if self.__isValidPosition(new_x, new_y):
            self.mouse_pos = (new_y, new_x)

    def getPressedButton(self):
        for button in self.buttons:
            if button.is_over(self.mouse_pos):
                return button
        return None
    
    def getMousePosition(self):
        return self.mouse_pos

    def __isValidPosition(self, x, y):
        return 0 <= x < WIDTH and 0 <= y < HEIGHT
