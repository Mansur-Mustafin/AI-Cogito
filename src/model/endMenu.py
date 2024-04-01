from model.button import Button
from settings import *
from model.state import State


class EndMenu(State):
    """
    Class that represents the model fo the end menu
    """

    def __init__(self, level) -> None:
        """
        EndMenu constructor
        :param level: Level that was completed
        :type level: Level
        :return: None
        """
        super().__init__()
        self.level = level

    def _create_buttons(self) -> None:
        """
        Creates the buttons for the level menu
        :return: None
        """
        self.buttons = [
            Button(None, None, W_BUTTON, H_BUTTON, "Play Again", WHITE_COLOR, BLUE_COLOR, 20),
            Button(None, None, W_BUTTON, H_BUTTON, "Go back to menu", WHITE_COLOR, BLUE_COLOR, 20),
        ]
