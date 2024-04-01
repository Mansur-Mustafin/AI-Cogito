import os

from model.button import Button
from settings import *
from model.state import State


class LevelMenu(State):
    """
    Class that represents the model for the level selection menu
    """
    def __init__(self, ai_algorithm = None, heuristic = None) -> None:
        """
        LevelMenu constructor
        :param ai_algorithm: algorithm that the AI uses
        :type ai_algorithm: enum AIS
        :param heuristic: heuristic that the AI uses
        :type heuristic: enum H
        :return: None
        """
        super().__init__()
        self.ai_algorithm = ai_algorithm
        self.heuristic = heuristic

    def _create_buttons(self) -> None:
        """
        Creates the buttons for the level menu
        :return: None
        """
        for filename in os.listdir(LEVELS_DIR):
            if filename.startswith("level") and filename.endswith(".yaml"):
                level_number = filename[5:-5]
                button_text = f"Level {level_number}"
                self.buttons.append(
                    Button(None, None, W_BUTTON * 0.6, H_BUTTON, button_text, BACKGROUND_COLOR, BLUE_COLOR, 20))
        self.buttons.sort(key=lambda button: int(button.text[6:]))
