import yaml
from settings import *
from model.state import State
from model.button import Button

class Level(State):
    COLORS = {'r', 'b', 'y'}

    def __init__(self, lvl):
        with open(LEVELS_DIR + "level" + str(lvl) + ".yaml", 'r') as file:
            level_data = yaml.safe_load(file)

        self.dimension = level_data['dimension']
        self.target_pattern = level_data['target_pattern']
        self.current_block = level_data['initial_block']
        self.main_color = level_data['main_color']
        self.blanck_color = level_data['blanck_color']
        self.score = 0
        self.cur_pos = (0, 0)
        self.level = lvl

        super().__init__()

    def _create_buttons(self) -> None:
        # copy from view
        scale = ((min(HEIGHT, WIDTH) - 5 * OFFSET) / ((H_SQUARE + GAP) * self.dimension))
        x_gap = scale * W_SQUARE + GAP
        y_gap = scale * H_SQUARE + GAP
        x_start = (WIDTH - W_LEFT_MENU - 2 * OFFSET) / 2 - (self.dimension * x_gap) / 2
        y_start = HEIGHT / 2 - (self.dimension * y_gap) / 2

        offset_button = (W_SQUARE * scale - ARROW_W) / 2

        # top
        x = x_start + offset_button
        y = y_start - ARROW_H
        for i in range(self.dimension):
            self.buttons.append(Button(x + i * x_gap , y,
                                  ARROW_W, ARROW_H, "↓", WHITE_COLOR, BLACK_COLOR, ARROW_FONT_S, ARROW_R, f"down {i}"))

        # right
        x = x_start + x_gap * self.dimension - GAP
        y = y_start + offset_button
        for i in range(self.dimension):
            self.buttons.append(Button(x, y + i * y_gap,
                                  ARROW_W, ARROW_H, "←", WHITE_COLOR, BLACK_COLOR, ARROW_FONT_S, ARROW_R, f"left {i}"))

        # buttom
        x = x_start + offset_button
        y = y_start + self.dimension * y_gap - GAP
        for i in range(self.dimension):
            self.buttons.append(Button(x + i * x_gap, y,
                                  ARROW_W, ARROW_H, "↑", WHITE_COLOR, BLACK_COLOR, ARROW_FONT_S, ARROW_R, f"up {i}"))

        # left
        x = x_start - ARROW_W
        y = y_start + offset_button
        for i in range(self.dimension):
            self.buttons.append(Button(x, y + i * y_gap,
                                  ARROW_W, ARROW_H, "→", WHITE_COLOR, BLACK_COLOR, ARROW_FONT_S, ARROW_R, f"right {i}"))


    def get_position(self) -> tuple[int, int]:
        """
        :return: The position of the player in the board
        :rtype: Tuple[Int, Int]
        """ 
        return self.cur_pos

    def get_dimension(self) -> int:
        """
        :return: The dimension of the board
        :rtype: Int
        """
        return self.dimension

    def get_level(self) -> int:
        """
        :return: The level number
        :rtype: Int
        """
        return self.level

    """
    :return: The current score
    :rtype: Int
    """

    def get_score(self) -> int:
        return self.score

    def increment_score(self):
        self.score += 1

    """
    :return: The current board
    :rtype: List[List[String]]
    """

    def get_current_board(self) -> list[list[str]]:
        return self.current_block

    """
    :return: The current board
    :rtype: List[List[String]]
    """

    def get_target_board(self) -> list[list[str]]:
        return self.target_pattern

    """
    :return: True if the current board is equal to the target board, false otherwise
    :rtype: Bool
    """

    def is_win_condition(self) -> bool:
        return self.current_block == self.target_pattern

    """
    :return: The number of blocks that differ from the current board to the target board
    :rtype: Int
    """

    def count_mismatched_tiles(self) -> int:
        return sum(
            self.current_block[i][j] != self.target_pattern[i][j]
            for i in range(self.dimension)
            for j in range(self.dimension)
        )

    def set_current_board(self, board):
        self.current_block = board        

    def get_value_at(self, row, col):
        return self.current_block[row][col]

    def get_main_color(self):
        return self.main_color


    def move_right(self, indx):
        self.current_block[indx] = [self.blanck_color] + self.current_block[indx][:-1]

    def move_left(self, indx):
        self.current_block[indx] = self.current_block[indx][1:] + [self.blanck_color]


    def move_down(self, indx):
        column = [row[indx] for row in self.current_block]
        shifted_column = [self.blanck_color] + column[:-1]
        for i, row in enumerate(self.current_block):
            row[indx] = shifted_column[i]


    def move_up(self, indx):
        column = [row[indx] for row in self.current_block]
        shifted_column = column[1:] + [self.blanck_color]
        for i, row in enumerate(self.current_block):
            row[indx] = shifted_column[i]
