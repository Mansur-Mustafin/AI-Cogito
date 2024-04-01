from model.button import Button
from settings import *
from model.state import State
from AI.ai import H


class HeuristicMenu(State):
    """
    Class that represents the model for the heuristics menu
    """

    def __init__(self, ai_algorithm=None) -> None:
        """
        Constructor for the Heuristics menu
        :param ai_algorithm: Algorithm that the AI uses
        :type ai_algorithm: enum AIS
        :return: None
        """
        super().__init__()
        self.ai_algorithm = ai_algorithm

    def _create_buttons(self) -> None:
        """
        Creates the buttons for the heuristic menu
        :return: None
        """
        self.buttons = [
            Button(None, None, W_BUTTON, H_BUTTON, 'Piece Mismatches', WHITE_COLOR, BLUE_COLOR, 20, action=H.MISS),
            Button(None, None, W_BUTTON, H_BUTTON, 'Line and Columns Diff.', WHITE_COLOR, BLUE_COLOR, 20,
                   action=H.LINECOLUMN),
            Button(None, None, W_BUTTON, H_BUTTON, 'Manhattan Distance', WHITE_COLOR, BLUE_COLOR, 20,
                   action=H.MANHATTAN),
            Button(None, None, W_BUTTON, H_BUTTON, 'Correct Row Pattern', WHITE_COLOR, BLUE_COLOR, 20,
                   action=H.PATTERN),
            Button(None, None, W_BUTTON, H_BUTTON, 'Manhattan with Pattern', WHITE_COLOR, BLUE_COLOR, 20,
                   action=H.MANHATTAN_PATTERN)
        ]
