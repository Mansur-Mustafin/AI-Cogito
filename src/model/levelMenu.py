import os
from model.button import Button
from model.menu import Menu
from .consts import *
from theme import *

class LevelMenu(Menu):

    def __init__(self):
        super().__init__()
        self.__create_buttons()

    """
    Creates the buttons for the level menu
    :return: None
    """

    def __create_buttons(self) -> None:
        i = 0
        for filename in os.listdir('levels/'):
            if filename.startswith("level") and filename.endswith(".yaml"):
                level_number = filename[5:-5]
                button_text = f"Level {level_number}"
                self.buttons.append(Button(X_BUTTON,Y_BUTTON + BUTTON_OFFSET *i ,W_BUTTON * 0.6, H_BUTTON, button_text, WHITE_COLOR, BLUE_COLOR, 20))
                i += 1
