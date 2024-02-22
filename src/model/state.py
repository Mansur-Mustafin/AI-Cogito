from abc import ABC, abstractmethod
import pygame
from settings import *
from model.button import Button
from typing import Optional


class State(ABC):

    def __init__(self):
        self.mouse_pos = (WIDTH / 2, HEIGHT / 2)
        self.buttons = []
        self._create_buttons()

    @abstractmethod
    def _create_buttons(self):
        pass

    def get_buttons(self) -> list[Button]:
        """
        :return: Buttons of the menu
        :rtype: list[Button]
        """
        return self.buttons

    def update_mouse_position(self, new_pos: tuple[int, int]) -> None:
        """
        Updates the mouse position
        :param new_pos: new mouse position
        :type new_pos: Tuple[Int,Int]
        :return: None
        """
        if self.__is_valid_position(new_pos[0], new_pos[1]):
            self.mouse_pos = new_pos

    def get_pressed_button(self) -> Optional[Button]:
        """
        :return: The button that has been pressed
        :rtype: Option[Button]
        """
        for button in self.buttons:
            if button.is_over(self.mouse_pos):
                return button
        return None

    def get_mouse_position(self) -> tuple[int, int]:
        """
        :return: The current mouse position
        :rtype: Tuple [Int,Int]
        """
        return self.mouse_pos

    @staticmethod
    def __is_valid_position(x: int, y: int) -> bool:
        """
        Verifies if the mouse position is valid
        :param x: horizontal position
        :type x: Int
        :param y: vertical position
        :type y: Int
        :return: True if the position is valid, False otherwise
        :rtype: Bool
        """
        return 0 <= x < WIDTH and 0 <= y < HEIGHT
