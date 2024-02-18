import yaml
from config import *


class Level:
    COLORS = {'r', 'b', 'y'}

    def __init__(self, lvl):
        with open(LEVELS_DIR + "level" + str(lvl) + ".yaml", 'r') as file:
            level_data = yaml.safe_load(file)

        self.dimension = level_data['dimension']
        self.target_pattern = level_data['target_pattern']
        self.current_block = level_data['initial_block']
        self.score = 0
        self.cur_pos = (0, 0)
        self.level = lvl

    """
    :return: The position of the player in the board
    :rtype: Tuple[Int, Int]
    """

    def get_position(self) -> tuple[int, int]:
        return self.cur_pos

    """
    :return: The dimension of the board
    :rtype: Int
    """

    def get_dimension(self) -> int:
        return self.dimension

    """
    :return: The level number
    :rtype: Int
    """

    def get_level(self) -> int:
        return self.level

    """
    :return: The current score
    :rtype: Int
    """

    def get_score(self) -> int:
        return self.score

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

    """
    Verifies if the player can execute a move and if so moves the player
    :param move: the move to be executed
    :type move: Tuple[Int,Int] 
    :return: None
    """

    def process_move(self, move: tuple[int, int]) -> None:
        d_x, d_y = move
        if self.__is_valid_move(d_x, d_y):

            x, y = self.cur_pos
            new_x, new_y = x + d_x, y + d_y

            self.cur_pos = (new_x, new_y)
            self.score += 1

            orig_color = self.current_block[y][x]
            dest_color = self.current_block[new_y][new_x]

            if orig_color != dest_color:
                third_color = (self.COLORS - {orig_color, dest_color}).pop()
                self.current_block[new_y][new_x] = third_color

    """
    Verifies if a move is valid
    :param d_x: horizontal movement
    :type d_x: int
    :param d_y: vertical movement
    :type d_y: int
    :return: True if the move is valid, false otherwise
    :rtype: Bool
    """

    def __is_valid_move(self, d_x: int, d_y: int) -> bool:
        new_x = self.cur_pos[0] + d_x
        new_y = self.cur_pos[1] + d_y
        return 0 <= new_x < self.dimension and \
            0 <= new_y < self.dimension and \
            self.current_block[new_x][new_y] is not None
