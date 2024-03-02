from model.button import Button
from settings import *
from model.state import State
from view.componets.buttons import buttonComponent

class MainMenu(State):

    def __init__(self):
        super().__init__()

    def _create_buttons(self) -> None:
        """
        Creates the buttons for the level menu
        :return: None
        """
        self.buttons = [
            Button("Play"),
            Button("DFS"),
            Button("BFS"),
            Button("Greedy"),
            Button("A* Algorithm"),
            Button("Weighted A* Algorithm"),
        ]
