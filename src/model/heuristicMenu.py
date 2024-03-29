import os
from model.button import Button
from settings import *
from model.state import State
from AI.ai import H

class HeuristicMenu(State):

    def __init__(self, ai_algorithm = None):
        super().__init__()
        self.ai_algorithm = ai_algorithm

    def _create_buttons(self) -> None:
        """
        Creates the buttons for the hueristic menu
        :return: None
        """
        self.buttons = [
            Button(None, None, W_BUTTON, H_BUTTON, 'Piece Mismatches', WHITE_COLOR, BLUE_COLOR, 20, action=H.MISS),
            Button(None, None, W_BUTTON, H_BUTTON, 'Line and Columns Diff.', WHITE_COLOR, BLUE_COLOR, 20, action=H.LINECOLUMN),
            Button(None, None, W_BUTTON, H_BUTTON, 'Manhattan Distance', WHITE_COLOR, BLUE_COLOR, 20, action=H.MANHATTAN),
            Button(None, None, W_BUTTON, H_BUTTON, 'Correct Row Pattern', WHITE_COLOR, BLUE_COLOR, 20, action=H.PATTERN)
        ]
