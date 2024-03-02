import os
from model.button import Button
from settings import *
from model.state import State


class LevelMenu(State):

    def __init__(self):
        super().__init__()

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
                    Button(button_text))
        self.buttons.sort(key=lambda button: int(button.text[6:]))
