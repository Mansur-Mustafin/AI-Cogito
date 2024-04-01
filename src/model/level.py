import yaml

from settings import *
from model.state import State
from model.button import Button


class Level(State):
    """
    The Level class represents the model of a level. It holds informations
    about the current and target board and other important information as the time it has passed
    the number of moves the player or AI has taken, etc.. It also defines some helper functions
    to retrieve or change information of the board.
    """

    COLORS = {'r', 'b'}

    def __init__(self, lvl: int, ai_algorithm, heuristic) -> None:
        """
        Level constructor
        :param lvl: Number of the level
        :type lvl: int
        :param ai_algorithm: Algorithm to be used by the AI
        :type ai_algorithm: enum AIS
        :param heuristic: Heuristic to be used by the AI
        :type heuristic: enum H
        :return: None
        :rtype: None
        """

        with open(LEVELS_DIR + "level" + str(lvl) + ".yaml", 'r') as file:
            level_data = yaml.safe_load(file)

        self.dimension = level_data['dimension']
        self.main_colors = level_data['main_color']
        self.current_block = self.__build_board(level_data['initial_block'])
        self.target_pattern = self.__build_board(level_data['target_pattern'])
        self.blank_color = level_data['blank_color']
        self.max = level_data['max']
        self.difficulty= level_data['difficulty']
        self.shift = level_data['shift']
        self.move_type = level_data['move_type']
        self.score = 0
        self.time = 0
        self.level = lvl
        self.selected_button = None # No button is selected at the beginning

        self.ai_algorithm = ai_algorithm
        self.heuristic = heuristic
        self.is_ai = ai_algorithm != None
        self.is_paused = False

        super().__init__()

    def __eq__(self, other: dict[tuple[int, int], chr]) -> bool: 
        """
        Level equality dunder method. Determines if a level is the same as another by comparing
        their current boards
        :param other: The other current board
        :type other: dict[tuple[int, int], chr]
        :return: True if the two levels are equal, false otherwise.
        :rtype: bool
        """
        if isinstance(other, self.__class__):
            return self.current_block == other.current_block and self.level == other.level
        else:
            return False

    def __hash__(self) -> int:
        """
        Level hash dunder method. Calculates the hash of a Level
        """
        current_block_tuple = tuple(tuple(row) for row in self.current_block)
        return hash((current_block_tuple , self.level)) 

    def __build_board(self, board: list[list[int]]) -> dict[tuple[int, int], chr]:
        """
        Builds a dictionary representing the board as a sparse matrix (the empty spaces aren't stored).
        :param board: 2D matrix representing the color of each tile in the board
        :type board: list[list[int]]
        :return: The board representation in a dictionary
        :rtype: dict[tuple[int, int], chr]
        """
        new_board = dict()
        for row in range(self.dimension):
            for col in range(self.dimension):
                piece = board[row][col]
                if piece in self.main_colors:
                    new_board[(row, col)] = piece

        return new_board

    def _create_buttons(self) -> None:
        """
        Creates the buttons necessary to interact with the game.
        """

        # copy from view
        scale = ((min(HEIGHT, WIDTH) - 5 * OFFSET) / ((H_SQUARE + GAP) * self.dimension))
        x_gap = scale * W_SQUARE + GAP
        y_gap = scale * H_SQUARE + GAP
        x_start = (WIDTH - W_LEFT_MENU - 2 * OFFSET) / 2 - (self.dimension * x_gap) / 2
        y_start = HEIGHT / 2 - (self.dimension * y_gap) / 2

        offset_button = (W_SQUARE * scale - ARROW_W) / 2

        self.buttons.append(Button(QUIT_X, QUIT_Y, W_BUTTON * 0.6, H_BUTTON, "Quit", BACKGROUND_COLOR, RED_COLOR, 20))
        if not self.is_ai:
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
            
            self.buttons.append(Button(QUIT_X, QUIT_Y - H_BUTTON - GAP*2, W_BUTTON * 0.6, H_BUTTON, "Help", BACKGROUND_COLOR, BLUE_COLOR, 20))
        else:
            self.buttons.append(Button(VIEW_ACTIONS_X + 2*(ICONS_SIZE + ACTIONS_SPACE), VIEW_ACTIONS_Y, ICONS_SIZE, ICONS_SIZE, action='Next_right', image='next_right.png'))
            self.buttons.append(Button(VIEW_ACTIONS_X, VIEW_ACTIONS_Y, ICONS_SIZE, ICONS_SIZE, action='Next_left', image='next_left.png'))
            # It is important that these are the last buttons to be appended to ease pause/unpause update 
            if self.is_paused:
                self.buttons.append(Button(VIEW_ACTIONS_X + ICONS_SIZE + ACTIONS_SPACE, VIEW_ACTIONS_Y, ICONS_SIZE, ICONS_SIZE, action='Resume', image='play.png'))
            else:
                self.buttons.append(Button(VIEW_ACTIONS_X + ICONS_SIZE + ACTIONS_SPACE, VIEW_ACTIONS_Y, ICONS_SIZE, ICONS_SIZE, action='Pause', image='pause.png'))

    def get_dimension(self) -> int:
        """
        :return: The dimension of the board
        :rtype: int
        """
        return self.dimension

    def get_level(self) -> int:
        """
        :return: The level's number
        :rtype: int
        """
        return self.level

    def get_score(self) -> int:
        """
        :return: The current number of moves played
        :rtype: int
        """
        return self.score

    def increment_score(self) -> None:
        """
        Increment the number of moves taken
        :return: None
        """
        self.score += 1

    def get_current_board(self) -> dict[tuple[int, int], chr]:
        """
        :return: The current board
        :rtype: dict[tuple[int, int], chr]
        """
        return self.current_block

    def get_target_board(self) -> dict[tuple[int, int], chr]:
        """
        :return: The target board
        :rtype: dict[tuple[int, int], chr]
        """
        return self.target_pattern

    def is_win_condition(self) -> bool:
        """
        :return: True if the current board is equal to the target board, false otherwise
        :rtype: bool
        """
        for key, color in self.current_block.items():
                if( (not (key in self.target_pattern.keys())) or  color != self.target_pattern[key][0]): 
                    return False
        return True

    def count_mismatched_tiles(self) -> int:
        """
        :return: The number of tiles that differ from the current board to the target board
        :rtype: int
        """
        total = 0
        for pos, color in self.current_block.items():
            if pos not in self.target_pattern or color != self.target_pattern[pos][0]:
                total += 1
        return total

    def set_current_board(self, board: dict[tuple[int, int], chr]) -> None:
        """
        Updates the current board
        :param board: New board
        :return: None
        """
        self.current_block = board

    def get_value_at(self, row: int, col: int) -> str:
        """
        :param row: index of the row
        :param col: index of the column
        :return: Color of tile in the current board at the given row and column
        """
        return self.current_block.get((row, col), self.blank_color)

    def get_main_colors(self) -> list[str]:
        """
        :return: Main colors used in the boards
        """
        return self.main_colors

    def get_board_row(self, row: int, is_curr_board: bool = True) -> list[tuple[tuple[int, int]], [chr]]:
        """
        :param row: index of the row
        :type row: int
        :param is_curr_board: True to fetch row in the current board, false to fetch row in the target board
        :type is_curr_board: bool
        :return: List of tuples with position and color of non-empty tiles desired row
        :rtype: list[tuple[tuple[int, int]][chr]]
        """
        res = []
        board = self.current_block if is_curr_board else self.target_pattern
        for y in range(self.dimension):
            if (row, y) in board:
                res.append(((row, y), board[(row, y)]))
        return res

    def get_board_col(self, col: int, is_curr_board: bool = True):
        """
        :param col: index of the column
        :type col: int
        :param is_curr_board: True to fetch column in the current board, false to fetch column in the target board
        :type is_curr_board: bool
        :return: List of tuples with position and color of non-empty tiles in desired column
        :rtype: list[tuple[tuple[int, int]][chr]]
        """
        res = []
        board = self.current_block if is_curr_board else self.target_pattern
        for x in range(self.dimension):
            if (x, col) in board:
                res.append(((x, col), board[(x, col)]))
        return res

    def move_row(self, idx: int, shift: int, move_mirrored: bool = False) -> dict[tuple[int, int], chr]:
        """
        :param idx: Index of selected row
        :type idx: int
        :param shift: Distance to shift each tile
        :type shift: int
        :param move_mirrored: True if the mirrored row should be moved
        :type move_mirrored: bool
        :return: The updated level after moving the row
        :rtype: dict[tuple[int, int], chr]
        """
        row = self.get_board_row(idx)
        for (x, y), piece in row:
            del self.current_block[(x, y)]

        for (x, y), piece in row:
            self.current_block[(x, (y + shift) % self.dimension)] = piece

        middle_row = (self.dimension - 1) / 2
        if move_mirrored and idx != middle_row:
            dist_to_middle_row = abs(middle_row - idx)
            mirrored_idx = middle_row + dist_to_middle_row if idx < middle_row else middle_row - dist_to_middle_row
            mirrored_row = self.get_board_row(mirrored_idx)

            for (x, y), piece in mirrored_row:
                del self.current_block[(x, y)]

            for (x, y), piece in mirrored_row:
                self.current_block[(x, (y + shift) % self.dimension)] = piece

        return self

    def move_col(self, idx: int, shift: int, move_mirrored: bool = False) -> dict[tuple[int, int], chr]:
        """
        :param idx: Index of selected column
        :type idx: int
        :param shift: Distance to shift each tile
        :type shift: int
        :param move_mirrored: True if the mirrored column should be moved
        :type move_mirrored: bool
        :return: The updated level after moving the column
        :rtype: dict[tuple[int, int], chr]
        """
        col = self.get_board_col(idx)
        for (x, y), piece in col:
            del self.current_block[(x, y)]

        for (x, y), piece in col:
            self.current_block[((x + shift) % self.dimension, y)] = piece

        middle_col = (self.dimension - 1) / 2
        if move_mirrored and idx != middle_col:
            dist_to_middle_col = abs(middle_col - idx)
            mirrored_idx = middle_col + dist_to_middle_col if idx < middle_col else middle_col - dist_to_middle_col
            mirrored_col = self.get_board_col(mirrored_idx)

            for (x, y), piece in mirrored_col:
                del self.current_block[(x, y)]

            for (x, y), piece in mirrored_col:
                self.current_block[((x + shift) % self.dimension, y)] = piece

        return self
    
    def get_row_pieces(self, idx: int, is_curr_board: bool = True) -> dict[str, int]:
        """
        Get the frequency of each tile in a specific row
        :param idx: Index of selected row
        :type idx: int
        :param is_curr_board: True to fetch from row in the current board, false to fetch from row in the target board
        :type is_curr_board: bool
        :return: A dictionary with the frequency of each tile color in the row
        :rtype: dict[str][int]
        """
        row = self.get_board_row(idx, is_curr_board)
        colors_freq = {color: 0 for color in self.COLORS}

        for cell in row:
            if cell[1][0] != 'y':
                colors_freq[cell[1][0]] += 1
        
        return colors_freq

    def get_col_pieces(self, idx: int, is_curr_board: bool = True) -> dict[str, int]:
        """
        Get the frequency of each tile in a specific column
        :param idx: Index of selected column
        :type idx: int
        :param is_curr_board: True to fetch from column in the current board, false to fetch from column in the target board
        :type is_curr_board: bool
        :return: A dictionary with the frequency of each tile color in the column
        :rtype: dict[str][int]
        """
        col = self.get_board_col(idx, is_curr_board)
        colors_freq = {color: 0 for color in self.COLORS}

        for cell in col:
            if cell[1][0] != 'y':
                colors_freq[cell[1][0]] += 1

        return colors_freq
    
    def manhattan_distance(self, pieceA: tuple[int, int], pieceB: tuple[int, int]) -> int:
        """
        :param pieceA: position of piece A
        :type pieceA: tuple[int][int]
        :param pieceB: position of piece B
        :type pieceB: tuple[int][int]
        :return: Manhattan distance between the positions of the two pieces
        :rtype: int
        """
        x1, y1 = pieceA
        x2, y2 = pieceB
        dx = min (abs(x2-x1),abs(self.dimension - (x2-x1)))
        dy = min (abs(y2-y1),abs(self.dimension - (y2-y1)))
        return dx + dy

    def lost(self) -> bool:
        """
        Checks if player has lost the game. A player loses the game if the amount of moves he has played
        surpasses the limit established by the level
        :return: True if the player has lost the game, false otherwise
        :rtype: bool
        """
        return self.max - self.score <= 0

    def select_button(self, move: str) -> None:
        """
        Selects a button depending on the move, updating the Level state
        :param move: Identifies the button that was pressed. Holds the direction and index of the button
        :type move: str
        :return: None
        :rtype: None
        """
        if move is None:
            return None

        shift = {
            "down" : 0,
            "left" : 1,
            "up" : 2,
            "right" : 3
        }
        dir, indx = move.split()

        idx_button = shift[dir] * self.dimension + int(indx)
        self.buttons[idx_button].selected = True
        self.selected_button = idx_button

    def unselect_button(self) -> None:
        """
        Unselects a button that was pressed, updating the Level state
        :return: None
        :rtype: None
        """
        if self.selected_button is not None:
            self.buttons[self.selected_button].selected = False
            self.selected_button = None

    def pause(self) -> None:
        """
        Pauses the view used to watch the moves player by the AI
        :return: None
        :rtype: None
        """
        self.is_paused = True
        self.buttons.pop()
        self.buttons.append(Button(VIEW_ACTIONS_X + ICONS_SIZE + ACTIONS_SPACE, VIEW_ACTIONS_Y, ICONS_SIZE, ICONS_SIZE, action='Resume', image='play.png'))
    
    def unpause(self) -> None:
        """
        Pauses the view used to watch the moves player by the AI
        :return: None
        :rtype: None
        """
        self.is_paused = False
        self.buttons.pop()
        self.buttons.append(Button(VIEW_ACTIONS_X + ICONS_SIZE + ACTIONS_SPACE, VIEW_ACTIONS_Y, ICONS_SIZE, ICONS_SIZE, action='Pause', image='pause.png'))
