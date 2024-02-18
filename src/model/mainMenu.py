from model.button import Button
from settings import *
from model.menu import Menu

class MainMenu(Menu):

    def __init__(self):
        super().__init__()
        self.__createButtons()
    
    """
    Creates the buttons for the level menu
    :return: None
    """
    def __createButtons(self) -> None:
        self.buttons = [
            Button(W_BUTTON, H_BUTTON, "Jogar", WHITE_COLOR, BLUE_COLOR, 20),
            Button(W_BUTTON, H_BUTTON, "Run AI (DFS)", WHITE_COLOR, BLUE_COLOR, 20),
            Button(W_BUTTON, H_BUTTON, "Run AI (BFS)", WHITE_COLOR, BLUE_COLOR, 20),
            Button(W_BUTTON, H_BUTTON, "Run AI (Greedy)", WHITE_COLOR, BLUE_COLOR, 20),
            Button(W_BUTTON, H_BUTTON, "Run AI (A* Algorithm)", WHITE_COLOR, BLUE_COLOR, 20),
            Button(W_BUTTON, H_BUTTON, "Run AI (Weighted A* Algorithm)", WHITE_COLOR, BLUE_COLOR, 20),
        ]

