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
        self.main_colors = level_data['main_color']
        self.blank_color = level_data['blank_color']
        self.score = 0
        self.time = 0
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
            self.buttons.append(Button(x + i * x_gap, y,
                                       ARROW_W, ARROW_H, "↓", WHITE_COLOR, BLACK_COLOR, ARROW_FONT_S, ARROW_R,
                                       f"down {i}"))

        # right
        x = x_start + x_gap * self.dimension - GAP
        y = y_start + offset_button
        for i in range(self.dimension):
            self.buttons.append(Button(x, y + i * y_gap,
                                       ARROW_W, ARROW_H, "←", WHITE_COLOR, BLACK_COLOR, ARROW_FONT_S, ARROW_R,
                                       f"left {i}"))

        # buttom
        x = x_start + offset_button
        y = y_start + self.dimension * y_gap - GAP
        for i in range(self.dimension):
            self.buttons.append(Button(x + i * x_gap, y,
                                       ARROW_W, ARROW_H, "↑", WHITE_COLOR, BLACK_COLOR, ARROW_FONT_S, ARROW_R,
                                       f"up {i}"))

        # left
        x = x_start - ARROW_W
        y = y_start + offset_button
        for i in range(self.dimension):
            self.buttons.append(Button(x, y + i * y_gap,
                                       ARROW_W, ARROW_H, "→", WHITE_COLOR, BLACK_COLOR, ARROW_FONT_S, ARROW_R,
                                       f"right {i}"))

        self.buttons.append(Button(QUIT_X, QUIT_Y, W_BUTTON * 0.6, H_BUTTON, "Quit", BACKGROUND_COLOR, RED_COLOR, 20))

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

    def get_score(self) -> int:
        """
        :return: The current score
        :rtype: Int
        """
        return self.score

    def increment_score(self) -> None:
        """
        Increment the score
        :return: None
        """
        self.score += 1

    def get_current_board(self) -> list[list[str]]:
        """
        :return: The current board
        :rtype: List[List[String]]
        """
        return self.current_block

    def get_target_board(self) -> list[list[str]]:
        """
        :return: The current board
        :rtype: List[List[String]]
        """
        return self.target_pattern

    def is_win_condition(self) -> bool:
        """
        :return: True if the current board is equal to the target board, false otherwise
        :rtype: Bool
        """
        return self.current_block == self.target_pattern

    def count_mismatched_tiles(self) -> int:
        """
        :return: The number of blocks that differ from the current board to the target board
        :rtype: Int
        """
        total = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                if (self.current_block[i][j] != self.target_pattern[i][j] and
                        self.target_pattern[i][j] in self.main_colors):
                    total += 1
        return total

    def set_current_board(self, board) -> None:
        """
        :param board: New board
        :return: None
        """
        self.current_block = board

    def get_value_at(self, row, col) -> str:
        """
        :param row:
        :param col:
        :return: Color value of the current block at the given row and column
        """
        return self.current_block[row][col]

    def get_main_colors(self) -> list[str]:
        """
        :return: Main colors
        """
        return self.main_colors

    def move_right(self, indx) -> None:
        """
        :param indx: Index of selected row
        :return:
        """
        self.current_block[indx] = [self.blank_color] + self.current_block[indx][:-1]

    def move_left(self, indx):
        """
        :param indx: Index of selected row
        :return:
        """
        self.current_block[indx] = self.current_block[indx][1:] + [self.blank_color]

    def move_down(self, indx):
        """
        :param indx: Index of selected column
        :return:
        """
        column = [row[indx] for row in self.current_block]
        shifted_column = [self.blank_color] + column[:-1]
        for i, row in enumerate(self.current_block):
            row[indx] = shifted_column[i]

    def move_up(self, indx):
        """
        :param indx: Index of selected column
        :return:
        """
        column = [row[indx] for row in self.current_block]
        shifted_column = column[1:] + [self.blank_color]
        for i, row in enumerate(self.current_block):
            row[indx] = shifted_column[i]
