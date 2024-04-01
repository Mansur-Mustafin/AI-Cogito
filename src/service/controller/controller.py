from abc import ABC, abstractmethod
from typing import Optional

import pygame

from view.view import View
from settings import *


class Controller(ABC):
    """
    An abstract base class representing a controller in a game architecture.
    Attributes:
    ----------
        state: The current state of the game or application.
        view: The view component associated with the game or application.
    """

    def __init__(self, state, view):
        """
        Initializes the Controller with the given state and view.

        :param state: The state of the game or application.
        :param view: The view of the game or application.
        """
        self.state = state
        self.view = view

    def handle_event(self) -> Optional[Command]:
        """
        Processes Pygame events and triggers corresponding actions.
        This method handles the quit event, mouse motion, and button presses.
        :return: Optional[Command]
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.WINDOWCLOSE:
                return Command.EXIT

            elif event.type == pygame.MOUSEMOTION:
                self.state.update_mouse_position(event.pos)
                return None

            elif event.type == pygame.MOUSEBUTTONDOWN:
                button = self.state.get_pressed_button()

                if button is None:
                    return None
                else:
                    return self.handle_pressed_button(button)

    @abstractmethod
    def handle_pressed_button(self, button) -> Optional[Command]:
        """
        An abstract method to be implemented by subclasses to define actions when a button is pressed.
        :param button: The button that was pressed.
        :return: Optional[Command]
        """
        pass

    def get_view(self) -> View:
        """
        Returns the current view of the controller.

        :return: The current view.
        """
        return self.view

    def get_state(self) -> any:
        """
        Returns the current state of the controller.

        :return: The current state.
        """
        return self.state

    def update_screen(self):
        """
        Draws the screen based on the current state and updates the Pygame display.
        """
        self.view.draw_screen(self.state)
        pygame.display.update()
