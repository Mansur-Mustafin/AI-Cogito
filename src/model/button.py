import pygame
from settings import *
from view.componets.buttons import buttonComponent

class Button:
    def __init__(self, text ='',action=None, component = buttonComponent):
        self.text = text
        self.component = component()
        self.action = action

    def __str__(self) -> str:
        return self.text

    def get_action(self):
        if self.action is None:
            return self.text
        else:
            return self.action


    def is_over(self, mouse_pos: tuple[int, int]) -> bool:
        """
        Checks if the mouse is over the button
        :param mouse_pos: the position of the mouse
        :type mouse_pos: Tuple[Int,Int]
        :return: True if the mouse is over the button, false otherwise
        :rtype: Bool
        """
        if self.component.x is None:
            return False
        # Pos is the mouse position as a tuple (x, y)
        if self.component.x < mouse_pos[0] < self.component.x + self.component.width and \
                self.component.y < mouse_pos[1] < self.component.y + self.component.height:
            return True
        return False
