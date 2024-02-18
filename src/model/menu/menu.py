import pygame
from config import *
from model.menu.button import Button
from typing import Optional
import os
from ..consts import *
from theme import *

MAIN_MENU_BUTTONS = lambda:  [
            Button(CENTER_X,Y_BUTTON,W_BUTTON, H_BUTTON, "Play", WHITE_COLOR, BLUE_COLOR, 20),
            Button(CENTER_X,Y_BUTTON + BUTTON_OFFSET + BUTTON_MARGIN ,W_BUTTON, H_BUTTON, "Run AI (DFS)", WHITE_COLOR, BLUE_COLOR, 20),
            Button(CENTER_X,Y_BUTTON + BUTTON_OFFSET + BUTTON_MARGIN *2 ,W_BUTTON, H_BUTTON, "Run AI (BFS)", WHITE_COLOR, BLUE_COLOR, 20),
            Button(CENTER_X,Y_BUTTON + BUTTON_OFFSET + BUTTON_MARGIN *3,W_BUTTON, H_BUTTON, "Run AI (Greedy)", WHITE_COLOR, BLUE_COLOR, 20),
            Button(CENTER_X,Y_BUTTON + BUTTON_OFFSET + BUTTON_MARGIN *4,W_BUTTON, H_BUTTON, "Run AI (A* Algorithm)", WHITE_COLOR, BLUE_COLOR, 20),
            Button(CENTER_X,Y_BUTTON + BUTTON_OFFSET + BUTTON_MARGIN *5,W_BUTTON, H_BUTTON, "Run AI (Weighted A* Algorithm)", WHITE_COLOR, BLUE_COLOR, 20),
]

LEVEL_MENU_BUTTONS = lambda :list(map(lambda filename, i: Button(X_BUTTON, Y_BUTTON + BUTTON_MARGIN * i, W_BUTTON * 0.6, H_BUTTON, f"Level {filename[5:-5]}", WHITE_COLOR, BLUE_COLOR, 20),
                                 filter(lambda filename: filename.startswith("level") and filename.endswith(".yaml"), 
                                        os.listdir('levels/')), 
                                 range(len(os.listdir('levels/')))))


class Menu:

    def __init__(self, buttons):
        self.mouse_pos = (WIDTH / 2, HEIGHT / 2)
        self.buttons = buttons

    def get_buttons(self) -> list[Button]:
        """
        :return: Buttons of the menu
        :rtype: list[Button]
        """
        return self.buttons

    """
    Updates the mouse position
    :param new_pos: new mouse position
    :type new_pos: Tuple[Int,Int]
    :return: None
    """

    def update_mouse_position(self, new_pos: tuple[int, int]) -> None:
        if self.__is_valid_position(new_pos[0], new_pos[1]):
            self.mouse_pos = new_pos

    """
    :return: The button that has been pressed
    :rtype: Option[Button]
    """

    def get_pressed_button(self) -> Optional[Button]:
        for button in self.buttons:
            if button.is_over(self.mouse_pos):
                return button
        return None

    """
    :return: The current mouse position
    :rtype: Tuple [Int,Int]
    """

    def get_mouse_position(self) -> tuple[int, int]:
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

    @staticmethod
    def __is_valid_position(x: int, y: int) -> bool:
        return 0 <= x < WIDTH and 0 <= y < HEIGHT
