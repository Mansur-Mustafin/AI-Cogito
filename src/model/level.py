import yaml
from settings import *
from model.state import State
from model.button import Button


class Level(State):
    # Para que temos isto se temos um field "main_color" no yaml?
    COLORS = {'r', 'b'}

    def __init__(self, lvl):
        with open(LEVELS_DIR + "level" + str(lvl) + ".yaml", 'r') as file:
            level_data = yaml.safe_load(file)

        self.dimension = level_data['dimension']
        self.main_colors = level_data['main_color']
        self.current_block = self.__build_board(level_data['initial_block'])
        self.target_pattern = self.__build_board(level_data['target_pattern'])
        self.blank_color = level_data['blank_color']
        self.max = level_data['max']
        self.difficulty= level_data['difficulty']
        self.score = 0
        self.time = 0
        self.level = lvl
        self.associated_pieces = self.associate_pieces()

        super().__init__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            for key, (color,_) in self.current_block.items():
                if( (not (key in self.target_pattern.keys())) or  color != self.target_pattern[key][0]): 
                    return False
            return True
        else:
            return False

    def __hash__(self):
        current_block_tuple = tuple(tuple(row) for row in self.current_block)
        return hash((current_block_tuple , self.level)) 

    def __build_board(self, board) -> dict[tuple[int, int], str]:
        """
        Builds a dictionary representing the board as a sparse matrix (the empty spaces aren't stored).
        :return: The board representation in a dictionary
        :rtype: Dict[Tuple[Int, Int], Chr]
        """
        new_board = dict()
        id = 0 
        for row in range(self.dimension):
            for col in range(self.dimension):
                piece = board[row][col]
                if piece in self.main_colors:
                    new_board[(row, col)] = (piece, id)
                    id +=1

        return new_board

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

    def get_current_board(self):
        """
        :return: The current board
        :rtype: List[List[String]]
        """
        return self.current_block

    def get_target_board(self):
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
        for key, (color,_) in self.current_block.items():
                if( (not (key in self.target_pattern.keys())) or  color != self.target_pattern[key][0]): 
                    return False
        return True

    def count_mismatched_tiles(self) -> int:
        """
        :return: The number of blocks that differ from the current board to the target board
        :rtype: Int
        """
        total = 0
        for pos, piece in self.current_block.items():
            if pos not in self.target_pattern or piece != self.target_pattern[pos]:
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
        return self.current_block.get((row, col), self.blank_color)

    def get_main_colors(self) -> list[str]:
        """
        :return: Main colors
        """
        return self.main_colors

    def get_board_row(self, row, is_curr_board=True):
        res = []
        board = self.current_block if is_curr_board else self.target_pattern
        for y in range(self.dimension):
            if (row, y) in board:
                res.append(((row, y), board[(row, y)]))
        return res

    def get_board_col(self, col, is_curr_board=True):
        res = []
        board = self.current_block if is_curr_board else self.target_pattern
        for x in range(self.dimension):
            if (x, col) in board:
                res.append(((x, col), board[(x, col)]))
        return res

    def move_row(self, idx, shift, move_mirrored=False):
        """
        :param idx: Index of selected row
        :param shift: Distance to shift each piece
        :param move_mirrored: True if the mirrored row should be moved
        :return: The updated level
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

    def move_col(self, idx, shift, move_mirrored=False):
        """
        :param idx: Index of selected column
        :param shift: Distance to shift each piece
        :param move_mirrored: True if the mirrored row should be moved
        :return: The updated level
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
    
    def get_row_pieces(self, idx, is_curr_board= True) -> dict:
        row = self.get_board_row(idx, is_curr_board)
        colors_freq = {color: 0 for color in self.COLORS}

        for cell in row:
            if cell[1][0] != 'y':
                colors_freq[cell[1][0]] += 1
        
        return colors_freq

    def get_col_pieces(self, idx, is_curr_board = True) -> dict:
        col = self.get_board_col(idx, is_curr_board)
        colors_freq = {color: 0 for color in self.COLORS}

        for cell in col:
            if cell[1][0] != 'y':
                colors_freq[cell[1][0]] += 1

        return colors_freq
    
    def manhattan_distance(self,pieceA, pieceB ):
        x1, y1 = pieceA
        x2, y2 = pieceB
        dx = min (abs(x2-x1),abs(self.dimension - (x2-x1)))
        dy = min (abs(y2-y1),abs(self.dimension - (y2-y1)))
        return dx + dy


    def associate_pieces(self):
        i = 0 
        associations = []
        for cord1, (color, _) in self.current_block.items():
            associations.append((0,0))
            min_dist = 2* self.dimension
            for cord2, (color2, _) in self.target_pattern.items():
                if( color == color2 and not (cord2 in associations)):
                    dist = self.manhattan_distance(cord1,cord2)
                    if ( min_dist > dist):
                        min_dist = dist
                        associations[i]= cord2
            i+=1
                

        return associations


    def is_valid_move(self, dir: str, indx: int) -> bool:
        if dir == "right":
            return not self.get_value_at(indx, -1) in self.get_main_colors()
        elif dir == "left":
            return not self.get_value_at(indx, 0) in self.get_main_colors()
        elif dir == "up":
            return not self.get_value_at(0, indx) in self.get_main_colors()
        elif dir == "down":
            return not self.get_value_at(-1, indx) in self.get_main_colors()
        else:
            print("[ERROR] Invalid move")
            return False
    
    def lost(self):
        return self.max - self.score <= 0

        
