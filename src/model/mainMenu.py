from model.button import Button
from settings import *
from model.state import State


class MainMenu(State):

    def __init__(self):
        super().__init__()

    def _create_buttons(self) -> None:
        """
        Creates the buttons for the level menu
        :return: None
        """
        self.buttons = [
            Button(None, None, W_BUTTON, H_BUTTON, "Play", WHITE_COLOR, BLUE_COLOR, 20),
            Button(None, None, W_BUTTON, H_BUTTON, "DFS", WHITE_COLOR, BLUE_COLOR, 20),
            Button(None, None, W_BUTTON, H_BUTTON, "BFS", WHITE_COLOR, BLUE_COLOR, 20),
            Button(None, None, W_BUTTON, H_BUTTON, "Greedy", WHITE_COLOR, BLUE_COLOR, 20),
            Button(None, None, W_BUTTON, H_BUTTON, "A* Algorithm", WHITE_COLOR, BLUE_COLOR, 20),
            Button(None, None, W_BUTTON, H_BUTTON, "Weighted A* Algorithm", WHITE_COLOR, BLUE_COLOR, 20),
        ]
