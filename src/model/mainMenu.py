from model.button import Button
from config import *
from model.menu import Menu
from .consts import *
from theme import *

class MainMenu(Menu):

    def __init__(self):
        super().__init__()
        self.__create_buttons()

    """
    Creates the buttons for the level menu
    :return: None
    """

    def __create_buttons(self) -> None:
        self.buttons = [
            Button(CENTER_X,Y_BUTTON,W_BUTTON, H_BUTTON, "Play", WHITE_COLOR, BLUE_COLOR, 20),
            Button(CENTER_X,Y_BUTTON + BUTTON_OFFSET ,W_BUTTON, H_BUTTON, "Run AI (DFS)", WHITE_COLOR, BLUE_COLOR, 20),
            Button(CENTER_X,Y_BUTTON + BUTTON_OFFSET *2 ,W_BUTTON, H_BUTTON, "Run AI (BFS)", WHITE_COLOR, BLUE_COLOR, 20),
            Button(CENTER_X,Y_BUTTON + BUTTON_OFFSET *3,W_BUTTON, H_BUTTON, "Run AI (Greedy)", WHITE_COLOR, BLUE_COLOR, 20),
            Button(CENTER_X,Y_BUTTON + BUTTON_OFFSET *4,W_BUTTON, H_BUTTON, "Run AI (A* Algorithm)", WHITE_COLOR, BLUE_COLOR, 20),
            Button(CENTER_X,Y_BUTTON + BUTTON_OFFSET *5,W_BUTTON, H_BUTTON, "Run AI (Weighted A* Algorithm)", WHITE_COLOR, BLUE_COLOR, 20),
        ]
