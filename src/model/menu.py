from abc import ABC, abstractmethod
import pygame
from settings import *
from .button import Button
from typing import Optional

class Menu(ABC):

    def __init__(self):
        self.mouse_pos = (WIDTH/2, HEIGHT/2)
        self.buttons = []

    """
    :return: Buttons of the menu
    :rtype: list[Button]
    """
    def getButtons(self) -> list[Button]:
        return self.buttons
    
    """
    Moves the user mouse
    :param d_x: horizontal movement
    :type d_x: Int
    :param d_y: vertical movement
    :type d_y: Int
    :return: None
    """
    def move_mouse(self, d_x:int, d_y:int)-> None:
        new_x = self.mouse_pos[0] + d_x
        new_y = self.mouse_pos[1] + d_y
        self.update_mouse_position(new_x, new_y)

    """
    Updates the mouse position
    :param new_pos: new mouse position
    :type new_pos: Tuple[Int,Int]
    :return: None
    """
    def update_mouse_position(self, new_pos: tuple[int,int])-> None:
        if self.__isValidPosition(new_pos[0], new_pos[1]):
            self.mouse_pos = new_pos

    """
    :return: The button that has been pressed
    :rtype: Option[Button]
    """
    def getPressedButton(self) -> Optional[Button]:
        for button in self.buttons:
            if button.is_over(self.mouse_pos):
                return button
        return None
    
    """
    :return: The current mouse position
    :rtype: Tuple [Int,Int]
    """
    def getMousePosition(self) -> tuple[int,int]:
        return self.mouse_pos

    """
    Verifies if the mouse position is valid
    :param x: horizontal position
    :type x: Int
    :param y: vertical position
    :type y: Int
    :return: True if the position is valid, False otherwise
    :rtype: Bool
    """
    def __isValidPosition(self, x:int, y:int) -> bool:
        return 0 <= x < WIDTH and 0 <= y < HEIGHT
