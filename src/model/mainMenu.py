from model.button import Button
from settings import *
from model.state import State
from AI.ai import AIS


class MainMenu(State):
    """
    Class that represents the model for the main menu
    """
    def __init__(self) -> None:
        """
        MainMenu constructor
        """
        super().__init__()

    def _create_buttons(self) -> None:
        """
        Creates the buttons for the level menu
        :return: None
        """
        self.buttons = [
            Button(None, None, W_BUTTON, H_BUTTON, "Play", WHITE_COLOR, BLUE_COLOR, 20),
            Button(None, None, W_BUTTON, H_BUTTON, "DFS", WHITE_COLOR, BLUE_COLOR, 20, action=AIS.DFS),
            Button(None, None, W_BUTTON, H_BUTTON, "BFS", WHITE_COLOR, BLUE_COLOR, 20, action=AIS.BFS),
            Button(None, None, W_BUTTON, H_BUTTON, "Iterative deepning DFS", WHITE_COLOR, BLUE_COLOR, 20, action=AIS.IDS),
            Button(None, None, W_BUTTON, H_BUTTON, "Greedy", WHITE_COLOR, BLUE_COLOR, 20, action=AIS.GREDDY),
            Button(None, None, W_BUTTON, H_BUTTON, "A* Algorithm", WHITE_COLOR, BLUE_COLOR, 20, action=AIS.ASTAR),
            Button(None, None, W_BUTTON, H_BUTTON, "Weighted A* Algorithm", WHITE_COLOR, BLUE_COLOR, 20, action=AIS.ASTARW),
        ]
